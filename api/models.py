# api/models.py
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class HealthMetric(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='metrics')
    weight = models.FloatField()
    blood_pressure = models.CharField(max_length=10)
    heart_rate = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.patient.name} - {self.date}"
