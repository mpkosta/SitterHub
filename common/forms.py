from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Вашето Име",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Имейл адрес",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'})
    )

    department = forms.CharField(
        initial="Отдел обслужване на клиенти",
        label="Насочено към",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bg-light',
                'readonly': 'readonly'
            }),
        help_text="Вашето запитване ще бъде обработено от нашия екип."
    )

    message = forms.CharField(
        label="Съобщение",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4})
    )