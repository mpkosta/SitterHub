from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from sitters.models import Sitter

class Application(models.Model):
    APPLICATION_STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview stage'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    ]

    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=50,
    )
    phone_number = models.CharField(
        max_length=20,
        blank=False,
    )
    email = models.EmailField()
    short_bio_introduction = models.TextField(
        help_text="Разкажете накратко за себе си!"
    )
    application_status = models.CharField(
        max_length=20,
        choices=APPLICATION_STATUS_CHOICES,
        default='applied',
    )
    created_at = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return (f"{self.first_name} {self.last_name} изпрати кандидатура "
                f"Текущ статус - {self.application_status}")

@receiver(post_save, sender=Application)
def create_sitter_on_hire(sender, instance, created, **kwargs):
    if instance.application_status == 'hired':
        sitter_exists = Sitter.objects.filter(
            sitter_first_name=instance.first_name,
            sitter_last_name=instance.last_name
        ).exists()

        if not sitter_exists:
            Sitter.objects.create(
                sitter_first_name=instance.first_name,
                sitter_last_name=instance.last_name,
                bio=instance.short_bio_introduction,
                hourly_rate=10.00
            )