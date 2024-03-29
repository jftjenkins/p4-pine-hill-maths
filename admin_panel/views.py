from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import AdminLogin

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
        # Logic to create a new student user based on form data
        # Example: user = User.objects.create(username=request.POST['username'], password=request.POST['password'])
        # Create an entry in the AdminLogin model to log the action
        AdminLogin.objects.create(user=request.user, action='Created a new student user')
        messages.success(request, 'Student user created successfully.')
        return redirect('manage_students')
    else:
        # Render the form to create a new student user
        return render(request, 'admin_panel/create_student.html')

@login_required
def view_student(request, student_id):
    """View function to view details of a specific student user."""
    # Logic to retrieve and display details of the specified student user
    return render(request, 'admin_panel/view_student.html', {'student_id': student_id})
