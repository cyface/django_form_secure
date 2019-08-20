"""
Models
"""
from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    message = models.TextField()
    message_creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    trip = models.ForeignKey('Trip', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.message[:23]


class Trip(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
