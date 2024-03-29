from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import StudentSignInForm

def student_authenticate(request):
    if request.method == 'POST':
        form = StudentSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('maths_lessons')  # Redirect to lessons.html
            else:
                error_message = "Invalid username or password. Please try again."
                return render(request, 'signin.html', {'form': form, 'error_message': error_message})
    else:
        form = StudentSignInForm()
    return render(request, 'signin.html', {'form': form})

