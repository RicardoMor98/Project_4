from django.urls import path
from .views import Bookings
from about.views import about


urlpatterns = [
    path('', Bookings.as_view(), name='bookings'),
    path('about/', about.as_view(), name='about'),
]