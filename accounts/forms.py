from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

UserModel = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email', 'phone_number')
        labels = {
            'email': 'Имейл адрес',
            'phone_number': 'Телефонен номер',
        }
        help_texts = {
            'email': 'Моля, въведете валиден имейл адрес. Ще се използва за възстановяване на парола.',
            'username': 'Уникално потребителско име (само букви, цифри и знаци @/./+/-/_).',
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Потребителско име или Имейл',
        widget=forms.TextInput(attrs={'autofocus': True})
    )