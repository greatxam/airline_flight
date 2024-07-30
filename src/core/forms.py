# Airline Flight
# Created by Maximillian M. Estrada on 2024-07-30

from django import forms

from core.models import *


class FlightForm(forms.ModelForm):
    aircraft = forms.ModelChoiceField(
        queryset=Aircraft.objects.all(),
        empty_label='-- Select Aircraft --',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    origin = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        empty_label='-- Select Origin --',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    destination = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        empty_label='-- Select Destination --',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    departure = forms.DateTimeField(
        input_formats=['%Y/%m/%d %I:%M %p'],
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control flatpickr datetimepicker',
            }
        )
    )

    arrival = forms.DateTimeField(
        input_formats=['%Y/%m/%d %I:%M %p'],
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control flatpickr datetimepicker',
            }
        )
    )

    class Meta:
        model = Flight
        fields = '__all__'
        exclude = ['flight_time',]
