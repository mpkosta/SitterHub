import time
from celery import shared_task

@shared_task
def send_contact_email_task(name, email, message):
    print(f"--- CELERY: Започвам обработка на запитване от {name} ({email}) ---")
    time.sleep(5)
    print(f"--- CELERY: Имейлът е изпратен успешно! Текст: {message[:15]}... ---")
    return "Done"