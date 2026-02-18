from django.db import models
from services.models import ServiceGroup

class Sitter(models.Model):
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
        upload_to='sitters_photos')

    def __str__(self):
        return f"{self.sitter_first_name}{self.sitter_last_name}"