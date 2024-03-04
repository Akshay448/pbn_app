from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .models import Patient
from .forms import PatientForm
from sqlalchemy_integration.engine import Session

from .serializers import PatientSerializer


# DRF ViewSet for API interactions
# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
# this gives error with the base model of patients with sqlalchemy

def list_patients(request):
    session = Session()
    try:
        patients = session.query(Patient).all()
        return render(request, 'patients/patient_list.html', {'patients': patients})
    finally:
        session.close()


def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            session = Session()
            try:
                patient = Patient(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    phone_number=form.cleaned_data['phone_number'],
                    date_of_birth=form.cleaned_data['date_of_birth'],
                )
                session.add(patient)
                session.commit()
                return redirect('list_patients')
            finally:
                session.close()
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})


def update_patient(request, pk):
    session = Session()
    patient = session.query(Patient).filter(Patient.id == pk).first()
    if patient is None:
        session.close()
        raise Http404("Patient not found")

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient.first_name = form.cleaned_data['first_name']
            patient.last_name = form.cleaned_data['last_name']
            patient.email = form.cleaned_data['email']
            patient.phone_number = form.cleaned_data['phone_number']
            patient.date_of_birth = form.cleaned_data['date_of_birth']
            session.commit()
            session.close()
            return redirect('list_patients')
    else:
        form = PatientForm(initial={
            'first_name': patient.first_name,
            'last_name': patient.last_name,
            'email': patient.email,
            'phone_number': patient.phone_number,
            'date_of_birth': patient.date_of_birth,
        })
    session.close()
    return render(request, 'patients/patient_form.html', {'form': form})


def delete_patient(request, pk):
    session = Session()
    patient = session.query(Patient).filter(Patient.id == pk).first()
    if patient is None:
        session.close()
        raise Http404("Patient not found")

    if request.method == 'POST':
        session.delete(patient)
        session.commit()
        session.close()
        return redirect('list_patients')
    else:
        session.close()
        return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})