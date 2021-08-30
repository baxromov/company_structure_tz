from django.views import generic

from . import models


class HomeView(generic.ListView):
    template_name = "pages/index.html"
    queryset = models.Department.objects.all()
    context_object_name = 'departments'
