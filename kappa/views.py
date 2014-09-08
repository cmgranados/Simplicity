from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render


@login_required
def kappa_home(request):
    return render(request, 'kappa_home.html')