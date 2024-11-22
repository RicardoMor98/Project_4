from django.shortcuts import render
from .models import Lesson

# Create your views here.

def home(request):
    lessons = Lesson.objects.all()
    return render(request, 'index.html', {'lessons': lessons})