from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import path, include
from student.models import ScoreCard
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout


@login_required
def scorecard(request):
    if request.method != 'GET':
        return redirect('home')

    username = request.GET.get('username', None)

    if username is not None and username != '':
        test_results = ScoreCard.objects.filter(username=username)
        return render(request, 'scorecard.html', {'test_results': test_results})

    if request.user.is_staff:
        test_results = ScoreCard.objects.all()
        return render(request, 'scorecard.html', {'test_results': test_results})

    test_results = ScoreCard.objects.filter(username=request.user)

    return render(request, 'scorecard.html', {'test_results': test_results})
