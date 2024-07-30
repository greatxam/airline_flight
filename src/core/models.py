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

