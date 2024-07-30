# Airline Flight
# Created by Maximillian M. Estrada on 2024-07-30
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.list import MultipleObjectMixin

from core.forms import FlightForm
from core.models import Flight


class DashboardView(TemplateView):
    template_name = 'core/index.html'


class FlightView(MultipleObjectMixin, CreateView):
    model = Flight
    template_name = 'core/flight.html'
    form_class = FlightForm
    success_url = reverse_lazy('core-flight')

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        return super().get_context_data(**kwargs)
