from django.urls import path
from patients import views

urlpatterns = [
    path('visit/<int:patient>',
        views.PatientViewVisits.as_view(),
        name='patient-visit'),
    path('',
        views.ViewPatients.as_view(),
        name='patients'),
    ]
