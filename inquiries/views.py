from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import InquiryForm
from sitters.models import Sitter
from .models import Inquiry
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy


def create_inquiry(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.sitter = sitter
            inquiry.save()
            messages.success(
                request,
                f"Успешно изпратихте запитване за {sitter.sitter_first_name} "
                f"{sitter.sitter_last_name}!")
            return redirect("sitters-list")
    else:
        form = InquiryForm()

    context = {
        "sitter": sitter,
        "form": form,
    }

    return render(request, 'inquiries/inquiry_form.html', context)
