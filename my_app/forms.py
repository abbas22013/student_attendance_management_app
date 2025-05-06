from django import forms
from .models import Class
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['instructor_name', 'room_number', 'class_code']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_number', 'major', 'status', 'class_id']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
