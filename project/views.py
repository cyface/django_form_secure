"""
Views
"""
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from forms import MessageForm
from project.models import Trip, Message


class TripDetail(DetailView):
    model = Trip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(trip=context.get('trip'))
        context['message_form'] = MessageForm(
            initial={'message_creator': self.request.user, 'trip': context.get('trip')})
        return context


class TripList(ListView):
    model = Trip


class MessageCreateView(CreateView):
    form_class = MessageForm
    template_name = "project/message_form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.message_creator = self.request.user
        # @TODO: Validate user has permissions to post messages on this trip
        return form

    def get_success_url(self):
        return reverse_lazy("trip_detail", args={self.object.trip_id})
        # @TODO: If you want to use this from elsewhere, you will need to pass in something so it knows where to go
