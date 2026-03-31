from django.db import models
from services.models import ServiceGroup
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Language(models.Model):
    language_name = models.CharField(
        max_length=50,
        unique=True)

    def __str__(self):
        return self.language_name

class Sitter(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='sitter_profile'
    )

    sitter_first_name = models.CharField(
        max_length=50
    )
    sitter_last_name = models.CharField(
        max_length=50
    )
    bio = models.TextField()
    services = models.ManyToManyField(
        ServiceGroup,
        related_name='sitters')
    experience = models.PositiveIntegerField(
        default=0)
    hourly_rate = models.DecimalField(
        max_digits=4,
        decimal_places=2)
    photo = models.ImageField(
        upload_to='sitters_photos',
        blank=True,
        null=True)
    languages = models.ManyToManyField(
        Language,
        related_name='sitters',
        blank=True
    )

    def __str__(self):
        return f"{self.sitter_first_name} {self.sitter_last_name}"