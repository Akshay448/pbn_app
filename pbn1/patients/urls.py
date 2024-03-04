from django.conf.urls import url, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'patients', views.PatientViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # url('api/', include(router.urls)),  # API endpoints withh viewset
    url('list/', views.list_patients, name='list_patients'),  # Web interface endpoints
    url('create/', views.create_patient, name='create_patient'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.update_patient, name='update_patient'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.delete_patient, name='delete_patient'),
]
