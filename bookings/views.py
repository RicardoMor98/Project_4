from django.views.generic import TemplateView


class Bookings(TemplateView):
    template_name = 'bookings/bookings.html'