from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Application
from .forms import ApplicationForm, ApplicationEditForm
from .tasks import send_status_update_email_task

class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = "recruitment/application_form.html"
    success_url = reverse_lazy("application-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Вашата кандидатура е изпратена успешно! Очаквайте отговор до няколко часа.")
        return super().form_valid(form)

class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = "recruitment/application_list.html"
    context_object_name = "applications"
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_staff:
            return Application.objects.all().order_by("-created_at")
        return Application.objects.filter(user=self.request.user).order_by("-created_at")

class ApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Application
    form_class = ApplicationEditForm
    template_name = "recruitment/application_form.html"
    success_url = reverse_lazy("application-list")

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user or self.request.user.is_staff

    def form_valid(self, form):
        response = super().form_valid(form)

        if 'application_status' in form.changed_data:
            send_status_update_email_task.delay(self.object.id)

        messages.success(self.request, "Кандидатурата е обновена успешно!")
        return response

class ApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Application
    template_name = "recruitment/application_delete.html"
    success_url = reverse_lazy("application-list")

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user or self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, "Кандидатурата беше изтрита успешно!")
        return super().form_valid(form)