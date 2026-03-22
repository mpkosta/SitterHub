import re
from django.core.exceptions import ValidationError

class SitterHubPasswordValidator:
    def validate(self, password, user=None):
        if not re.search(r'\d', password):
            raise ValidationError(
                "Паролата трябва да съдържа поне една цифра.",
                code='password_without_number',
            )
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "Паролата трябва да съдържа поне една главна буква.",
                code='password_without_uppercase',
            )

    def get_help_text(self):
        return "Вашата парола трябва да съдържа минимум една главна буква и една цифра."