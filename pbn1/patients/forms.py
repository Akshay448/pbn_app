from django import forms
from .models import Patient

# used with viewset
# class PatientForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth']


from django import forms

class PatientForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    date_of_birth = forms.DateField()
