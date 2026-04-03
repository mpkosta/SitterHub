from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InquiryForm
from .models import Inquiry
from sitters.models import Sitter
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


class InquiryCreateView(LoginRequiredMixin, CreateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = 'inquiries/inquiry_form.html'
    success_url = reverse_lazy('inquiry-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sitter'] = get_object_or_404(Sitter, pk=self.kwargs.get('sitter_id'))
        return context

    def form_valid(self, form):
        sitter = get_object_or_404(Sitter, pk=self.kwargs.get('sitter_id'))
        form.instance.sitter = sitter
        form.instance.user = self.request.user

        messages.success(
            self.request,
            f"Успешно изпратихте запитване за {sitter.sitter_first_name} {sitter.sitter_last_name}!"
        )
        return super().form_valid(form)


class InquiryListView(LoginRequiredMixin, ListView):
    model = Inquiry
    template_name = "inquiries/inquiry_list.html"
    context_object_name = "inquiries"
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        queryset = Inquiry.objects.filter(user=user)

        try:
            if hasattr(user, 'sitter_profile'):
                queryset = queryset | Inquiry.objects.filter(sitter=user.sitter_profile)
        except ObjectDoesNotExist:
            pass

        return queryset.order_by("-created_at").distinct()


class InquiryUpdateView(LoginRequiredMixin, UpdateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = "inquiries/inquiry_form.html"
    success_url = reverse_lazy("inquiry-list")

    def get_queryset(self):
        return Inquiry.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Запитването е обновено успешно!")
        return super().form_valid(form)


class InquiryDeleteView(LoginRequiredMixin, DeleteView):
    model = Inquiry
    template_name = "inquiries/inquiry_delete.html"
    success_url = reverse_lazy("inquiry-list")

    def get_queryset(self):
        return Inquiry.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Запитването беше изтрито успешно!")
        return super().delete(request, *args, **kwargs)