from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def maths_lessons_view(request):
    # Your view logic here
    return render(request, 'maths_lessons/lessons.html', context)
