# Airline Flight
# Created by Maximillian M. Estrada on 2024-07-30

from django.urls import path

from core.views import *

urlpatterns = [
    # dashboard
    path(
        '',
        DashboardView.as_view(),
        name='core-dashboard'),
    # flight
    path(
        'flights/',
        FlightView.as_view(),
        name='core-flight'),
]
