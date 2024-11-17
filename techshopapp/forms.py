from django import forms
from .models import User


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'email']

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 14:
            raise forms.ValidationError('Возраст должен быть больше 14')
        return age

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == "admin":
            raise forms.ValidationError('Имя не должно быть admin')
        return name

