from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home_view(request):
    return render(request, 'common/home.html')

def about_view(request):
    return render(request, 'common/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            messages.success(
                request,
                "Вашето съобщение беше изпратено успешно! Ще се свържем с вас до няколко часа.")
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'common/contact.html', {'form': form})