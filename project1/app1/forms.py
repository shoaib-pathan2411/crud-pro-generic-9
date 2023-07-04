from django import forms
from .models import Student
from django.core import validators


def chek_name(value):
    if value.istitle() == False:
        raise validators.ValidationError('name should be starts with capital letter')

class StudentForm(forms.ModelForm):
    name = forms.CharField(validators=[chek_name])
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'address':forms.Textarea(),
            'email':forms.EmailInput(),
            'birth_date':forms.DateInput(attrs={'type':'date'}),
            'password':forms.PasswordInput(),
            'c_password':forms.PasswordInput()
        }

    def clean(self):
        data = super().clean()
        p1 = data['password']
        p2 = data['c_password']
        if p1 != p2:
            raise validators.ValidationError('password and confirm password should be same')
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise validators.ValidationError('age should be greater than 18')
        return age