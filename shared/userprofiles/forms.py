# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput


class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)

	class Meta:
		model = User
		fields = ('username','email','first_name','last_name')
	
	def __init__(self, *args, **kwargs):
		super(UserCreationEmailForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].label = "Nombres"
		self.fields['last_name'].label = "Apellidos"
		self.fields['password2'].help_text = "Introduzca de nuevo la contraseña para su verificación."
		

class EmailAuthenticationForm(forms.Form):
	email = forms.EmailField(label="Correo electrónico", widget=TextInput(attrs={'class': 'form-control',
                            'required': 'true',
                            'placeholder': ''
    }))
	password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control',
                            'required': 'true',
                            'placeholder': ''
    }))

	def __init__(self, *args, **kwargs):
		self.user_cache = None
		super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

	def clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')

		self.user_cache = authenticate(email=email, password=password)

		if self.user_cache is None:
			raise forms.ValidationError("Usuario incorrecto")
		elif not self.user_cache.is_active:
			raise forms.ValidationError("Usuario inactivo")

		return self.cleaned_data

	def get_user(self):
		return self.user_cache
