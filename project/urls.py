"""django_form_secure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required

from project.views import TripList, TripDetail, MessageCreateView

urlpatterns = [
    path('', RedirectView.as_view(url="/trips/"), name="home"),
    path('admin/', admin.site.urls),
    path('trips/', login_required(TripList.as_view()), name="trip_list"),
    path('messages/add/', login_required(MessageCreateView.as_view()), name="message_create"),
    path('trips/<int:pk>/', login_required(TripDetail.as_view()), name="trip_detail"),
]
