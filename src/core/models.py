# Airline Flight
# Created by Maximillian M. Estrada on 2024-07-30

import uuid

from django.conf import settings
from django.db import models


class BaseAbstract(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    created = models.DateTimeField(
        auto_now_add=True)
    modified = models.DateTimeField(
        auto_now=True)


class Aircraft(BaseAbstract):
    class Meta:
        db_table = 'core_aircrafts'
        ordering = ['name']

    name = models.CharField(
        unique=True,
        max_length=100)

    def __str__(self):
        return self.name


class Airport(BaseAbstract):
    class Meta:
        db_table = 'core_airports'
        ordering = ['name']

    name = models.CharField(
        unique=True,
        max_length=100)

    def __str__(self):
        return self.name


class Flight(BaseAbstract):
    class Meta:
        db_table = 'core_flights'
        ordering = ['created']

    aircraft = models.ForeignKey(
        'Aircraft',
        on_delete=models.CASCADE)
    origin = models.ForeignKey(
        'Airport',
        related_name='origin',
        on_delete=models.CASCADE)
    destination = models.ForeignKey(
        'Airport',
        related_name='destination',
        on_delete=models.CASCADE)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    flight_time = models.DurationField()

    def save(self, *args, **kwargs):
        self.flight_time = self.arrival - self.departure
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.aircraft.name}: {self.origin.name} - {self.destination.name}"
