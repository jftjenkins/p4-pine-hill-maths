from django.shortcuts import render, redirect, get_object_or_404
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
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('dashboard')

            # Invalid credentials
        messages.error(request, 'Invalid username or password for teacher login. Please try again.')

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
            hashed_password = make_password(password)
            new_user = User.objects.create(username=username, email=email, password=hashed_password)
            new_user.save()
            messages.success(request, 'Student added successfully.')
            return redirect('create_student')
    else:
        form = StudentForm()
    return render(request, 'teacher/create_students.html', {'form': form})

@login_required
@staff_member_required
def view_students(request):
    students = User.objects.filter(is_staff=False)
    return render(request, 'teacher/view_students.html', {'students': students})

@login_required
@staff_member_required
def edit_student(request, student_id):
    student = get_object_or_404(User, id=student_id, is_staff=False)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student.username = form.cleaned_data['username']
            student.email = form.cleaned_data['email']
            password = form.cleaned_data.get('password')
            if password:
                student.password = make_password(password)
            student.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('view_students')
        else:
            print("Form is not valid")
            print("Form errors:", form.errors)
    else:
        form = StudentForm(instance=student)
    return render(request, 'teacher/view_students.html', {'form': form, 'student': student})

@login_required
@staff_member_required
def delete_student(request, student_id):
    student = get_object_or_404(User, id=student_id, is_staff=False)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully.')
        return redirect('view_students')
    return redirect('view_students')
