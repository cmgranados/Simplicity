from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render


@login_required
def omicron_home(request):
    return render(request, 'omicron_home.html')