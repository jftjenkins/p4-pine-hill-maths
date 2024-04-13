from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import TeacherCreationForm
from .models import Teacher

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Try to authenticate against the default User model
            user = authenticate(request, username=username, password=password)
            if user is None:
                # Try to authenticate against the Teacher model
                teacher = Teacher.objects.filter(username=username).first()
                if teacher is not None and teacher.check_password(password):
                    user = teacher
                    
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')  # Redirect all authenticated users to the admin dashboard
            else:
                # Invalid credentials
                return redirect('admin_login')
        else:
            # Form is not valid
            error_message = 'Username or password is incorrect. If you are struggling to login, please contact <a href="mailto:ithelpdesk@pinehillsgs.com">ithelpdesk@pinehillsgs.com</a>.'
            messages.error(request, error_message, extra_tags='safe')
            return render(request, 'admin_panel/admin_login.html', {'form': form})
    else:
        # GET request
        form = AuthenticationForm()
        return render(request, 'admin_panel/admin_login.html', {'form': form})

def admin_dashboard(request):
    return render(request, 'admin_panel/dashboard.html')

def manage_students(request):
    return render(request, 'admin_panel/manage_students.html')

def create_student(request):
    return render(request, 'admin_panel/create_students.html')

def view_students(request):
    return render(request, 'admin_panel/view_students.html')