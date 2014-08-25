from django.shortcuts import render_to_response, render


def kappa_home(request):
    return render(request, 'kappa_home.html')