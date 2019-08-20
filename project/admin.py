from django.contrib import admin
from django.contrib.auth.models import User

from project.models import Message, Trip


class UserInline(admin.StackedInline):
    model = User


class MessageInline(admin.StackedInline):
    model = Message


class TripAdmin(admin.ModelAdmin):
    inlines = [MessageInline]


admin.site.register(Trip, TripAdmin)
