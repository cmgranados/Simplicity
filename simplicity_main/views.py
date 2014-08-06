from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout as auth_logout
from django.http.response import HttpResponseRedirect


def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')
