from django.db import models

from sitters.models import Sitter


# Create your models here.

class Inquiry(models.Model):
    client_first_name = models.CharField(
        max_length=50)
    client_last_name = models.CharField(
        max_length=50
    )
    client_phone = models.CharField(
        max_length=20)
    client_email = models.EmailField(
        blank=True,
        null=True,)
    sitter = models.ForeignKey(
        Sitter,
        on_delete=models.CASCADE,
        related_name='inquiries',
    )
    message = models.TextField(
        help_text='Кратко съобщение към нашия детегледач',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.client_first_name} {self.client_last_name} is inquiring  about "
                f"{self.sitter.first_name}")