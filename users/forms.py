from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    # username = forms.CharField(
    #     label='Имя пользователя',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   "class": "form-control",
    #                                   "placeholder": "Введите имя пользователя"},)
    # )
    # password = forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       "class": "form-control",
    #                                       "placeholder": "Введите ваш пароль"
    #                                       }),
    # )
    class Meta:
        model = User
        fields = ['username', 'password']

# class CreateUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'age', 'email']
#
#     def clean_age(self):
#         age = self.cleaned_data['age']
#         if age < 14:
#             raise forms.ValidationError('Возраст должен быть больше 14')
#         return age
#
#     def clean_name(self):
#         name = self.cleaned_data['name']
#         if name == "admin":
#             raise forms.ValidationError('Имя не должно быть admin')
#         return name

