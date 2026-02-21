from django.views.generic import ListView
from .models import Sitter
from services.models import ServiceGroup

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