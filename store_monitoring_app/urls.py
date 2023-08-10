
# store_monitoring_app/urls.py

from django.urls import path
from store_monitoring_app import views

urlpatterns = [
    path('trigger_report/', views.trigger_report, name='trigger_report'),
    path('get_report/', views.get_report, name='get_report'),
]