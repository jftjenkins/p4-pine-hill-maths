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
    # Dummy data for questions
    questions = [
        {'question': '2 + 2', 'answer': '4', 'id': 'Q1'},
        {'question': '10 - 5', 'answer': '5', 'id': 'Q2'},
        {'question': '3 * 5', 'answer': '15', 'id': 'Q3'},
        {'question': '20 / 4', 'answer': '5', 'id': 'Q4'},
        {'question': '7 + 3', 'answer': '10', 'id': 'Q5'},
        {'question': '15 - 7', 'answer': '8', 'id': 'Q6'},
        {'question': '6 * 4', 'answer': '24', 'id': 'Q7'},
        {'question': '40 / 5', 'answer': '8', 'id': 'Q8'},
        {'question': '9 + 6', 'answer': '15', 'id': 'Q9'},
        {'question': '18 - 9', 'answer': '9', 'id': 'Q10'},
    ]

    # Add index to each question
    for i, question in enumerate(questions):
        question['index'] = i + 1

    if request.method == 'POST':
        submitted_answers = request.POST.getlist('answers')
        correct_answers = [question['answer'] for question in questions]
        correct_count = sum(1 for sub, corr in zip(submitted_answers, correct_answers) if sub.lower() == corr.lower())

        # Prepare results for display
        results = [{'submitted': sub, 'correct': corr} for sub, corr in zip(submitted_answers, correct_answers)]

        return render(request, 'student_lessons/question_page.html', {'questions': questions, 'results': results, 'correct_count': correct_count})

    return render(request, 'student_lessons/question_page.html', {'questions': questions, 'results': None, 'correct_count': None})

