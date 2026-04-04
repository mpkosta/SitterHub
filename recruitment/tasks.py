from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Application


@shared_task
def send_status_update_email_task(application_id):
    try:
        app = Application.objects.get(id=application_id)

        subject = "Агенция Гледачи - Статус на кандидатура"

        if app.application_status == 'interview':
            message = f"Здравейте {app.first_name},\n\nВашата кандидатура е одобрена за етап 'Интервю'. Моля, очаквайте обаждане от наш сътрудник."
        elif app.application_status == 'rejected':
            message = f"Здравейте {app.first_name},\n\nБлагодарим ви за интереса, но за съжаление не продължавате напред в процеса."
        elif app.application_status == 'hired':
            message = f"Поздравления {app.first_name}!\n\nВие успешно преминахте всички етапи и сте част от нашия екип!"
        else:
            return "No email needed"

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[app.email],
            fail_silently=False,
        )
        return f"Email sent to {app.email} - Status: {app.application_status}"

    except Application.DoesNotExist:
        return "Application not found"