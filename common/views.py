from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .tasks import send_contact_email_task

def home_view(request):
    return render(request, 'common/home.html')

def about_view(request):
    return render(request, 'common/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name', 'Anonymous')
            email = form.cleaned_data.get('email', 'No email')
            message = form.cleaned_data.get('message', '')

            send_contact_email_task.delay(name, email, message)

            messages.success(
                request,
                "Вашето съобщение беше прието! Нашата система го обработва и ще се свържем с вас."
            )
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'common/contact.html', {'form': form})