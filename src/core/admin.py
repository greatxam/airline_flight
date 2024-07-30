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


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    search_fields = [
        'name',
    ]


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = [
        'aircraft',
        'origin',
        'destination',
        'flight_time',
    ]
    search_fields = [
        'aircraft__name',
        'origin__name',
        'destination__name',
    ]
    list_filter = [
        'aircraft',
        'origin',
        'destination',
    ]


admin.site.site_title = admin.site.site_header = "Airline Flight"
