# api/urls.py
from django.urls import path
from .views import PatientListCreateAPIView, HealthMetricListCreateAPIView

urlpatterns = [
    path('patients/', PatientListCreateAPIView.as_view(), name='patient-list-create'),
    path('health-metrics/', HealthMetricListCreateAPIView.as_view(), name='health-metric-list-create'),
]
