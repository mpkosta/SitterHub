from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            "first_name",
            "last_name",
            "short_bio_introduction",
            "phone_number",
            "email",
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': "Име"}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': "Фамилия"}),
            'short_bio_introduction': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': "Разкажете накратко за себе си!",
                       'rows': 4}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': "Телефонен номер"}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': "Имейл адрес"}),
        }

        labels = {
            "first_name": 'Име',
            "last_name": 'Фамилия',
            "short_bio_introduction": "Разкажете накратко за себе си!",
            "phone_number": 'Телефонен номер',
            "email": 'Имейл адрес',
        }

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        bio = cleaned_data.get("short_bio_introduction")
        phone = cleaned_data.get("phone_number")

        if first_name and not first_name.isalpha():
                self.add_error(
                    "first_name",
                    "Името ви трябва да съдържа само букви."
                )

        if last_name and not last_name.isalpha():
                self.add_error(
                    "last_name",
                    "Фамилията ви трябва да съдържа само букви."
                )


        if bio and len(bio) < 20:
            self.add_error(
                "short_bio_introduction",
                "Моля разкажете малко повече за себе си."
            )

        if phone and len(phone) < 10:
            self.add_error(
                "phone_number",
                "Телефонният ви номер трябва да съдържа поне 10 цифри.")

        return cleaned_data

class ApplicationEditForm(ApplicationForm):
    class Meta(ApplicationForm.Meta):
        fields = ApplicationForm.Meta.fields + ['application_status']
        widgets = {
            **ApplicationForm.Meta.widgets,
            'application_status': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            **ApplicationForm.Meta.labels,
            'application_status': 'Статус на кандидатурата',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].disabled = True