from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            "client_first_name",
            "client_last_name",
            "client_email",
            "message"
        ]

        widgets = {
            "client_first_name": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Име'}),
            "client_last_name": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Фамилия'}),
            "client_phone": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Телефонен номер'}),
            "client_email": forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Имейл адрес'}),
            "message": forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Моля изпратете кратко съобщение към нашият гледач'}),
        }

        labels = {
            "client_first_name": "Вашето Име",
            "client_last_name": "Вашата Фамилия",
            "client_email": "Имейл адрес (не е задължителен)",
            "message": "Вашето съобщение",
        }

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("client_phone")
        message = cleaned_data.get("message")

        if phone and len(phone) < 10:
            self.add_error(
                "client_phone",
                "Телефонният ви номер трябва да съдържа 10 цифри.")

        if message and len(message) < 20:
            self.add_error(
                "message",
                "Моля въведете повече информация за вашето запитване."
            )

        return cleaned_data