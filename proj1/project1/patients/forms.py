from django import forms
from patients.models import Patient, Location, Visit
from django.core.validators import MaxValueValidator, MinValueValidator


class PatientCreateForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget = forms.SelectDateWidget)
    date_case_confirmed = forms.DateField(widget = forms.SelectDateWidget)
    ID_number = forms.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(9999999)])
    class Meta:
        model = Patient
        fields = '__all__'

class LocationCreateForm(forms.ModelForm):
    x_coord = forms.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(99999)])
    y_coord = forms.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(99999)])
    class Meta:
        model = Location
        fields = '__all__'

class VisitCreateForm(forms.ModelForm):
    date_from = forms.DateField(widget = forms.SelectDateWidget)
    date_to = forms.DateField(widget = forms.SelectDateWidget)
    class Meta:
        model = Visit
        exclude = ['patient']
