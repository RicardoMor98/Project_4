from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lesson(models.Model):
    date = models.DateField()
    time = models.TimeField()
    coach_name = models.CharField(max_length=100)
    max_guests = models.IntegerField()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    num_guests = models.IntegerField()