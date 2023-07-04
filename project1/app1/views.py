from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required, name='dispatch')
class StudentView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('show_url')

@method_decorator(login_required, name='dispatch')
class ShowView(ListView):
    model = Student

@method_decorator(login_required, name='dispatch')
class UpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('show_url')

@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('show_url')

class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'app1/user_form.html'
    success_url = reverse_lazy('loginpage_url')






