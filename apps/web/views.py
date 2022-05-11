from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class LearnView(TemplateView):
    template_name = "learn.html"


class AboutView(TemplateView):
    template_name = "about.html"
