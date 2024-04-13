from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import StudentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Create your views here.
def teacher_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                # Invalid credentials
                error_message = 'Invalid username or password. Please try again.'
                return render(request, 'teacher/teacher_login.html', {'form': form, 'error_message': error_message})
        else:
            # Form is not valid
            return render(request, 'teacher/teacher_login.html', {'form': form})
    else:
        # GET request
        form = AuthenticationForm()
        return render(request, 'teacher/teacher_login.html', {'form': form})


@login_required
@staff_member_required
def dashboard(request):
    return render(request, 'teacher/dashboard.html')


@login_required
@staff_member_required
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Hash the password securely
            hashed_password = make_password(password)

            # Create new user with hashed password
            new_user = User.objects.create(username=username, email=email, password=hashed_password)
            new_user.save()

            messages.success(request, 'Student added successfully.')
            return render(request, 'teacher/create_students.html', {'form': form})
    else:
        form = StudentForm()
    return render(request, 'teacher/create_students.html', {'form': form})


@login_required
@staff_member_required
def view_students(request):
    students = User.objects.filter(is_staff=False)  # Filter out staff members (teachers)
    return render(request, 'teacher/view_students.html', {'students': students})
