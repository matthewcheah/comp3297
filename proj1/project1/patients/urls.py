from django.urls import path
from patients import views

urlpatterns = [
    path('visit/<int:patient>',
        views.PatientViewVisits.as_view(),
        name='patient_visit'),
    path('',
        views.ViewPatients.as_view(),
        name='patients'),
    path('locations',
        views.ViewLocations.as_view(),
        name = 'locations')
    ]
