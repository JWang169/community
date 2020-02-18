from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy  # in case someone is logged in or logged out, where should the page go
from django.views.generic import CreateView

from . import forms


# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')  # after a user is signed up, reverse to the login page
    template_name = 'accounts/signup.html'


