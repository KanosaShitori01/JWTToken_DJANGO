from django.views.generic import TemplateView
# Create your views here.
class RenderHome(TemplateView):
    template_name = "index.html"