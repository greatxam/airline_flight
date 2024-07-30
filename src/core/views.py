# Airline Flight
# Created by Maximillian M. Estrada on 2024-07-30

from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'core/index.html'
