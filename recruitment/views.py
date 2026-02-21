from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Application
from .forms import ApplicationForm, ApplicationEditForm

class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = "recruitment/application_form.html"
    success_url = reverse_lazy("application-list")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Вашата кандидатура е изпратена успешно! Очаквайте отговор до няколко часа.")

        return super().form_valid(form)

class ApplicationListView(ListView):
    model = Application
    template_name = "recruitment/application_list.html"
    context_object_name = "applications"
    ordering = "-created_at",
    paginate_by = 10

class ApplicationUpdateView(UpdateView):
    model = Application
    form_class = ApplicationEditForm
    template_name = "recruitment/application_form.html"
    success_url = reverse_lazy("application-list")

    def form_valid(self, form):
        messages.success(self.request, "Вашата кандидатура е обновена успешно!")
        return super().form_valid(form)

class ApplicationDeleteView(DeleteView):
    model = Application
    template_name = "recruitment/application_delete.html"
    success_url = reverse_lazy("application-list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Вашата кандидатура беше изтрита успешно!")
        return super().delete(request, *args, **kwargs)