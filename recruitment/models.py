from django.db import models

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
        help_text="Разкажи накратко за себе си!"
    )
    application_status = models.CharField(
        max_length=20,
        choices=APPLICATION_STATUS_CHOICES,
        default='applied',
    )
    created_at = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return (f"{self.first_name} {self.last_name} submitted an application! "
                f"Current status - {self.application_status}")