# Airline Flight
# Created by Maximillian M. Estrada on 2024-07-30

from django.views.generic import ListView, TemplateView

from core.models import Flight


class DashboardView(TemplateView):
    template_name = 'core/index.html'


class FlightView(ListView):
    model = Flight
    template_name = 'core/flight.html'

