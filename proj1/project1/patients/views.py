from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from patients.forms import LocationCreateForm, PatientCreateForm, VisitCreateForm
from patients.models import Patient,Visit,Location
from django.views.generic.list import ListView

# Create your views here.
class PatientViewVisits(TemplateView):
    template_name = "visit_list.html"
    def get(self, request, **kwargs):
        form = VisitCreateForm()
        patient = self.kwargs['patient']
        #print(patient)
        # print 1
        visit_list = Visit.objects.filter(patient__pk = patient)
        patient = Patient.objects.get(pk = patient)
        #print(patient)
        # print john jones
        args = {'form':form,'visit_list': visit_list,'patient':patient}
        #print(args)
        return render(request, self.template_name, args)

    def post(self,request,patient):
        #print(type(patient))
        form = VisitCreateForm(request.POST)
        if form.is_valid():
            form_of_visits = form.save(commit=False)
            form_of_visits.patient = Patient.objects.get(pk = patient)
            form.save()
        form = VisitCreateForm()
        url = "/patients/visit/{}".format(patient)
        return redirect(url)


class ViewPatients(ListView):
    template_name = "patient_list.html"
    def get(self,request):
            form = PatientCreateForm()
            patient = Patient.objects.all()
            args = {'form':form,'patient_list':patient}
            return render(request, self.template_name, args)

    def post(self,request):
            form = PatientCreateForm(request.POST)
            if form.is_valid():
                form.save()
            form = PatientCreateForm()
            return redirect('/patients/')



class ViewLocations(ListView):
    template_name = "location_list.html"
    def get(self,request):
            form = LocationCreateForm()
            location = Location.objects.all()
            args = {'form':form,'location_list':location}
            return render(request, self.template_name, args)

    def post(self,request):
            form = LocationCreateForm(request.POST)
            if form.is_valid():
                form.save()
            form = LocationCreateForm()
            return redirect('/patients/locations')
