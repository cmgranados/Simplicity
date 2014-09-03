from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render

from simplicity_main.constants import MyConstants
from simplicity_main.views import index

from .forms import UserCreationEmailForm, EmailAuthenticationForm


def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		requirement_analyst_group = Group.objects.get(name=MyConstants.GROUP_REQUIREMENT_ANALYST_NAME) 
		requirement_analyst_group.user_set.add(form.save())

	return render(request, 'signup.html', {'form': form})


def signin(request):
	if request.user.is_authenticated():
		return index(request)
	else:
		form = EmailAuthenticationForm(request.POST or None)
		
		if form.is_valid():
			login(request, form.get_user())
			return index(request)
		else:
			return render(request, 'signin.html', {'form': form})
	
