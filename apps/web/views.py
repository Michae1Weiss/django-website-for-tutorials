from pathlib import Path
import markdown

from django.http import Http404
from django.conf import settings
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, DetailView, ListView

from .models import Tutorial


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        md = settings.BASE_DIR / settings.STATIC_ROOT / 'md' / 'homepage.md'
        with md.open('r') as f:
            context['markdown'] = markdown.markdown(f.read())
        return context


class AboutView(TemplateView):
    template_name = "about.html"


class TutorialView(DetailView):
    model = Tutorial
    template_name = "tutorial.html"

    def get_object(self, queryset=None):
        # Use a custom queryset if provided.
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by `day`.
        day = self.kwargs.get("day")
        if day is not None:
            queryset = queryset.filter(day=day)

        # If `day` is None, it's an error.
        if day is None:
            raise AttributeError(
                "Generic detail view %s must be called an object "
                "day in the URLconf." % self.__class__.__name__
            )

        try:
            # Get the single item from the filtered queryset.
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['markdown'] = markdown.markdown(self.object.text)
        return context


class TutorialsView(ListView):
    model = Tutorial
    template_name = "tutorial_list.html"


class CSSExampleView(TemplateView):
    template_name = "mini-css-usage-example.html"
