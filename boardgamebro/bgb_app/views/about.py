from django.views.generic import TemplateView


class About(TemplateView):
    template_name = 'about/about.html'
