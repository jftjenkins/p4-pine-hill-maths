from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import MathsLesson, ScoreCard
from django.contrib.auth import get_user_model
import random

User = get_user_model()

def student_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("lessons")  # Redirect to lessons page after login
        else:
            messages.error(
                request,
                "Invalid username or password for student login. Please try again.",
            )
    else:
        form = AuthenticationForm()
    return render(request, "student/signin.html", {"form": form})

@login_required
def get_all_lesson(request):
    # Retrieve all available maths lessons from the database
    lessons = MathsLesson.objects.all()
    return render(request, "student/lessons.html", {"lessons": lessons})

def get_random_question(question_type, difficulty):
    min_num = 100
    max_num = 500
    questions = []

    if difficulty == "level_2":
        min_num = -500
        max_num = 500
    elif difficulty == "level_3":
        min_num = 5000
        max_num = 20000

    for index in range(1, 11):
        if question_type == "multiplication":
            if difficulty == "level_1":
                num1 = random.randint(1, 999)
                num2 = random.randint(1, 10)
            elif difficulty == "level_2":
                num1 = random.randint(-999, 999)
                num2 = random.randint(-10, 10)
            else:  # Level 3 or others
                num1 = random.randint(min_num, max_num)
                num2 = random.randint(min_num, max_num)
        elif question_type == "division":
            if difficulty == "level_1":
                num2 = random.randint(1, 10)
                num1 = num2 * random.randint(1, 100)
            elif difficulty == "level_2":
                num2 = random.randint(-10, 10)
                if num2 == 0:  # Avoid division by zero
                    num2 = 1
                num1 = num2 * random.randint(-100, 100)
            else:  # Level 3 or others
                num1 = random.randint(min_num, max_num)
                num2 = random.randint(1, 1000)
        else:
            num1 = random.randint(min_num, max_num)
            num2 = random.randint(min_num, max_num)

        if difficulty == "level_3":
            num1 = num1 / random.choice([1, 10, 100, 1000])
            num2 = num2 / random.choice([1, 10, 100, 1000])
        if question_type == "addition":
            question = f"{num1} + {num2}"
            answer = str(num1 + num2)
        elif question_type == "subtraction":
            if difficulty == "level_1":
                num1, num2 = max(num1, num2), min(num1, num2)  # Ensure positive result
            question = f"{num1} - {num2}"
            answer = str(num1 - num2)
        elif question_type == "multiplication":
            question = f"{num1} × {num2}"
            answer = str(num1 * num2)
        elif question_type == "division":
            question = f"{num1} ÷ {num2}"
            answer = str(num1 / num2)
        else:
            continue
        questions.append({"question": question, "answer": answer, "index": index})
    return questions

@login_required
def get_question_page(request, question_type, difficulty):
    if request.method == "GET":
        questions = get_random_question(question_type, difficulty)
        return render(
            request,
            "student/question_page.html",
            {
                "questions": questions,
                "question_type": question_type,
                "difficulty": difficulty,
            },
        )

    elif request.method == "POST":
        questions = request.POST.getlist("question[]")
        correct_answers = request.POST.getlist("correct_answer[]")
        user_answers = request.POST.getlist("answers[]")

        output = []  # List to store output for each question
        total_marks = len(questions)
        score = 0  # Initialize score

        for question, correct_answer, user_answer in zip(
            questions, correct_answers, user_answers
        ):
            is_correct = False
            try:
                if round(float(correct_answer), 5) == round(float(user_answer), 5):
                    is_correct = True
                    score += 1
                output.append(
                    {
                        "question": question,
                        "correct_answer": correct_answer,
                        "user_answer": user_answer,
                        "is_correct": is_correct,
                    }
                )
            except (ValueError, TypeError) as e:
                output.append(
                    {
                        "question": question,
                        "correct_answer": correct_answer,
                        "user_answer": user_answer,
                        "is_correct": is_correct,
                        "error": str(e),  # Optionally log the error message
                    }
                )

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
            percentage_score=percentage_score,
        )
        test_result.save()
        return render(
            request,
            "student/question_page.html",
            {
                "questions": [],
                "output": output,
                "question_type": question_type,
                "difficulty": difficulty,
            },
        )
