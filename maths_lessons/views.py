from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import MathsLesson

def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lessons')  # Redirect to lessons page after login
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'student_lessons/signin.html', {'form': form})

def lessons(request):
    # Retrieve all available maths lessons from the database
    lessons = MathsLesson.objects.all()
    return render(request, 'student_lessons/lessons.html', {'lessons': lessons})

def question_page(request, type, difficulty):
    # dummy data
    questions = [
        {'question': '2 + 2', 'answer': '4'},
        {'question': '10 - 5', 'answer': '5'},
        {'question': '3 * 5', 'answer': '15'},
        {'question': '20 / 4', 'answer': '5'},
    ]

    # Add index to each question
    for i, question in enumerate(questions):
        question['index'] = i + 1

    return render(request, 'student_lessons/question_page.html', {'questions': questions})

