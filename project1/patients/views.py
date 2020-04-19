from django.shortcuts import render
from django.views.generic import TemplateView
from patients.models import Patient,Visit,Location
from django.views.generic.list import ListView

# Create your views here.
class PatientViewVisits(TemplateView):
    template_name = "visit_list.html"
    def get_context_data(self, **kwargs):
        patient = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        context['visit_list'] = Visit.objects.filter(patient__pk = patient)
        context['patient'] = Patient.objects.get(pk = patient)
        return context

class ViewPatients(ListView):
    template_name = "patient_list.html"
    model = Patient
