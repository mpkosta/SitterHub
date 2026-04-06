from django import forms
from .models import Sitter, Language
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class SitterProfileUpdateForm(forms.ModelForm):
    languages_input = forms.CharField(
        required=False,
        label='Говорими езици',
        help_text='Въведете езици, разделени със запетая (напр. Английски, Немски)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Английски, Немски, Испански'
        })
    )

    class Meta:
        model = Sitter
        fields = [
            'sitter_first_name',
            'sitter_last_name',
            'bio',
            'services',
            'experience',
            'hourly_rate',
            'photo',
        ]

        labels = {
            'sitter_first_name': 'Име',
            'sitter_last_name': 'Фамилия',
            'bio': 'За мен (Био)',
            'services': 'Предлагани услуги',
            'experience': 'Опит (в години)',
            'hourly_rate': 'Часова ставка (лв/ч)',
            'photo': 'Профилна снимка',
        }

        widgets = {
            'sitter_first_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Вашето име'}),
            'sitter_last_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Вашата фамилия'}),
            'bio': forms.Textarea(
                attrs={'class': 'form-control',
                       'rows': 5,
                       'placeholder': 'Разкажете за вас'}),
            'experience': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Години опит(въведете 0 ако е по-малко от година)'}),
            'hourly_rate': forms.NumberInput(
                attrs={'class': 'form-control'}),
            'services': forms.CheckboxSelectMultiple(),
            'photo': forms.FileInput(
                attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hourly_rate'].disabled = True
        self.fields['hourly_rate'].help_text = "Почасовото заплащане се редактира само от администратор."

        if self.instance and self.instance.pk:
            existing_langs = self.instance.languages.all()
            self.fields['languages_input'].initial = ', '.join([lang.language_name for lang in existing_langs])

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("sitter_first_name")
        last_name = cleaned_data.get("sitter_last_name")
        experience = cleaned_data.get("experience")
        bio = cleaned_data.get("bio")

        if first_name and not first_name.isalpha():
            self.add_error("sitter_first_name", "Името трябва да съдържа само букви.")

        if last_name and not last_name.isalpha():
            self.add_error("sitter_last_name", "Фамилията трябва да съдържа само букви.")

        if experience is not None and experience < 0:
            self.add_error("experience", "Опитът не може да бъде отрицателно число.")

        if bio and len(bio) < 30:
            self.add_error("bio", "Моля, въведете по-подробно описание (минимум 30 символа).")

        return cleaned_data

    def save(self, commit=True):
        sitter = super().save(commit=commit)

        if commit:
            langs_string = self.cleaned_data.get('languages_input', '')
            lang_names = [name.strip().capitalize() for name in langs_string.split(',') if name.strip()]
            sitter.languages.clear()

            for name in lang_names:
                lang_obj, created = Language.objects.get_or_create(language_name=name)
                sitter.languages.add(lang_obj)

        return sitter

class SitterCreateAdminForm(SitterProfileUpdateForm):
    class Meta(SitterProfileUpdateForm.Meta):
        fields = ['user'] + SitterProfileUpdateForm.Meta.fields
        labels = {
            **SitterProfileUpdateForm.Meta.labels,
            'user': 'Избери потребителски акаунт',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = UserModel.objects.filter(sitter_profile__isnull=True)
        self.fields['user'].widget.attrs.update({'class': 'form-select'})
        self.fields['hourly_rate'].disabled = False
        self.fields['hourly_rate'].help_text = "Въведете стартова часова ставка."