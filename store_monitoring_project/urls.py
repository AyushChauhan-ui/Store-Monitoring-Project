"""
URL configuration for store_monitoring_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# store_monitoring_project/urls.py

from django.urls import path
from store_monitoring_app import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line for the root path
    path('api/trigger_report', views.trigger_report, name='trigger_report'),
    path('api/get_report', views.get_report, name='get_report'),
]
