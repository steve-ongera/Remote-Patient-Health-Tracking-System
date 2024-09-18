from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import generics
from .models import Patient, HealthMetric
from .serializers import PatientSerializer, HealthMetricSerializer

class PatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class HealthMetricListCreateAPIView(generics.ListCreateAPIView):
    queryset = HealthMetric.objects.all()
    serializer_class = HealthMetricSerializer
