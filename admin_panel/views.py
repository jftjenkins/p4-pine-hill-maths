from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import TeacherCreationForm

def admin_login(request):
    if request.method == 'POST':
        form = TeacherCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                # Invalid credentials
                error_message = 'Invalid username or password. Please try again.'
                return render(request, 'admin_panel/admin_login.html', {'form': form, 'error_message': error_message})
        else:
            # Form is not valid
            return render(request, 'admin_panel/admin_login.html', {'form': form})
    else:
        # GET request
        form = TeacherCreationForm()
        return render(request, 'admin_panel/admin_login.html', {'form': form})


def admin_dashboard(request):
    return render(request, 'admin_panel/dashboard.html')

def manage_students(request):
    return render(request, 'admin_panel/manage_students.html')

def create_student(request):
    return render(request, 'admin_panel/create_students.html')

def view_students(request):
    return render(request, 'admin_panel/view_students.html')
