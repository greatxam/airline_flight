# Airline Flight
# Created by Maximillian M. Estrada on 2024-07-30

from django.contrib import admin
from core.models import *


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    search_fields = [
        'name',
    ]


admin.site.site_title = admin.site.site_header = "Airline Flight"
