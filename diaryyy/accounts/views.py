# accounts views.py

from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from . import forms

class SignUp (CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name='accounts/signup.html'
