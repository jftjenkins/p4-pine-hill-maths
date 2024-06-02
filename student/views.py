from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import MathsLesson, ScoreCard
from django.contrib.auth.forms import UserCreationForm
import random
from django.contrib.auth import get_user_model

User = get_user_model()


def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lessons')  # Redirect to lessons page after login
        else:
            messages.error(request, 'Invalid username or password for student login. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'student/signin.html', {'form': form})


@login_required
def get_all_lesson(request):
    # Retrieve all available maths lessons from the database
    lessons = MathsLesson.objects.all()
    return render(request, 'student/lessons.html', {'lessons': lessons})


def get_random_question(question_type, difficulty):
    min_num = 100
    max_num = 500
    questions = []

    if difficulty == 'level_2':
        min_num = -500
        max_num = 500
    elif difficulty == 'level_3':
        min_num = 5000
        max_num = 20000

    for index in range(1, 11):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        if difficulty == 'level_3':
            num1 = num1 / random.choice([1, 10, 100, 1000])
            num2 = num2 / random.choice([1, 10, 100, 1000])
        if question_type == 'addition':
            question = f"{num1} + {num2}"
            answer = str(num1 + num2)
        elif question_type == 'subtraction':
            question = f"{num1} -  {num2}"
            answer = str(num1 - num2)
        elif question_type == 'multiplication':
            question = f"{num1} × {num2}"
            answer = str(num1 * num2)
        elif question_type == 'division':
            question = f"{num1} ÷  {num2}"
            answer = str(num1 / num2)
        else:
            continue
        questions.append({'question': question, 'answer': answer, 'index': index})
    return questions

@login_required
def get_question_page(request, question_type, difficulty):
    if request.method == 'GET':
        questions = get_random_question(question_type, difficulty)
        return render(request, 'student/question_page.html', {'questions': questions, 'question_type': question_type, 'difficulty': difficulty})

    elif request.method == 'POST':
        questions = request.POST.getlist('question[]')
        correct_answers = request.POST.getlist('correct_answer[]')
        user_answers = request.POST.getlist('answers[]')

        output = []  # List to store output for each question
        total_marks = len(questions)
        score = 0  # Initialize score

        for question, correct_answer, user_answer in zip(questions, correct_answers, user_answers):
            is_correct = False
            try:
                if round(float(correct_answer), 5) == round(float(user_answer), 5):
                    is_correct = True
                    score += 1
                output.append({'question': question, 'correct_answer': correct_answer, 'user_answer': user_answer,
                               'is_correct': is_correct})

            except:
                output.append({'question': question, 'correct_answer': correct_answer, 'user_answer': user_answer,
                               'is_correct': is_correct})

        # Calculate percentage score
        percentage_score = (score / total_marks) * 100 if total_marks > 0 else 0

        # Create a record in the database for the test result
        test_result = ScoreCard.objects.create(
            username=request.user.username,
            email=request.user.email,
            test_type=question_type,
            difficulty=difficulty,
            total_questions=total_marks,
            score=score,
            percentage_score=percentage_score
        )
        test_result.save()
        return render(request, 'student/question_page.html', {'questions': [], 'output': output, 'question_type': question_type, 'difficulty': difficulty})


