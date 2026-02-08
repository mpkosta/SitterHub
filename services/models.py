from django.db import models
from django.utils.text import slugify


class ServiceGroup(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True)
    description = models.TextField(
        blank=True,
        help_text='Кратко описание на услугата', )
    slug = models.SlugField(
        unique=True,
        blank=True)
    icon = models.ImageField(
        upload_to='service_icons',
        blank=True,
        null=True)

    class Meta:
        verbose_name_plural = 'Service Groups'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name