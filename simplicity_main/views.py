from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render

from shared.userprofiles.forms import EmailAuthenticationForm


def index(request):
    form = EmailAuthenticationForm(request.POST or None)
        
    if form.is_valid():
        login(request, form.get_user())
        return render_to_response('home/index.html', context_instance=RequestContext(request)) 
    else:
        return render(request, 'home/index.html', {'form': form})

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')
