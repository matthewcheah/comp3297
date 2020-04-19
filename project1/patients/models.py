from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200)
    ID_number = models.CharField(max_length=10)
    date_of_birth = models.DateTimeField()
    date_case_confirmed = models.DateTimeField()
    def __str__(self):
        return self.name

class Location(models.Model):
    location_visited = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    x_coord = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(99999)])
    y_coord = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(99999)])
    detail = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.location_visited

class Visit(models.Model):
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return  f'{self.location} ({self.date_from})'
