from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View  # Import the View class
from .models import AdminLogin, Student
from .forms import AdminLoginForm  # Import the form for admin login
import random
import string

@login_required
def admin_dashboard(request):
    """View function for the admin dashboard."""
    # Retrieve data for the admin dashboard
    recent_logins = AdminLogin.objects.order_by('-timestamp')[:5] # Retrieve recent login activities

    context = {
        'recent_logins': recent_logins,  # Pass the recent login activities to the template
    }

    # Render the admin dashboard template with the context data
    return render(request, 'admin_panel/dashboard.html', context)

@login_required
def manage_students(request):
    """View function to manage student users."""
    # Logic to retrieve and manage student users
    return render(request, 'admin_panel/manage_students.html')

@login_required
def create_student(request):
    """View function to create a new student user."""
    if request.method == 'POST':
        # Generate a unique username and password for the student user
        username = Student.generate_unique_username()
        password = Student.generate_unique_password()
        # Create a new student user
        student = Student.objects.create_student(username=username, password=password)
        # Log the action
        AdminLogin.objects.create(user=request.user, action=f'Created a new student user: {student.username}')
        messages.success(request, 'Student user created successfully.')
        return redirect('manage_students')
    else:
        # Render the form to create a new student user
        return render(request, 'admin_panel/create_student.html')

@login_required
def view_students(request, student_id):
    """View function to view details of a specific student user."""
    # Logic to retrieve and display details of the specified student user
    return render(request, 'admin_panel/view_student.html', {'student_id': student_id})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate the user against the superadmin account
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                # Login the superadmin user
                login(request, user)
                return redirect('admin_dashboard')
            else:
                # Display error message for invalid credentials
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AdminLoginForm()
    return render(request, 'admin_panel/admin_login.html', {'form': form})


# Add the AdminLoginView class for rendering admin login page
class AdminLoginView(View):
    template_name = 'admin_panel/admin_login.html'

    def get(self, request, *args, **kwargs):
        form = AdminLoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            # Handle form submission
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Verify superadmin credentials
            if username == 'Superadmin' and password == 'superadmin_password':
                # Redirect to admin dashboard
                return redirect('admin_dashboard')
            else:
                # Display error message for invalid credentials
                messages.error(request, 'Invalid username or password. Please try again.')
        return render(request, self.template_name, {'form': form})
