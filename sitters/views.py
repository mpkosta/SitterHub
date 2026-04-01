from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Sitter
from services.models import ServiceGroup
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SitterProfileUpdateForm, SitterCreateAdminForm

class SitterListView(ListView):
    model = Sitter
    template_name = "sitters/sitters_list.html"
    context_object_name = "sitters"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related("services")
        service_category_slug = self.request.GET.get("service_category_slug")

        if service_category_slug:
            queryset = queryset.filter(services__slug=service_category_slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ServiceGroup.objects.all()
        return context

class SitterDetailView(DetailView):
    model = Sitter
    template_name = "sitters/sitter_profile.html"
    context_object_name = "sitter"


class SitterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sitter
    form_class = SitterProfileUpdateForm
    template_name = 'sitters/sitter_form.html'

    def test_func(self):
        sitter = self.get_object()
        return self.request.user == sitter.user

    def get_success_url(self):
        return reverse_lazy('sitters-list')

    def form_valid(self, form):
        messages.success(self.request, "Профилът ви беше обновен успешно!")
        return super().form_valid(form)


class SitterCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Sitter
    form_class = SitterCreateAdminForm
    template_name = 'sitters/sitter_form.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse_lazy('sitters-list')

    def form_valid(self, form):
        messages.success(self.request, "Гледачът беше добавен успешно в системата!")
        return super().form_valid(form)