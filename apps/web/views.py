from django.http import Http404
from django.conf import settings
from django.views.generic import TemplateView, DetailView, ListView, FormView
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import FileFieldModelForm
from .models import Tutorial, Exercise


class MarkdownTemplateView(TemplateView):
    """Returns `markdown` content in context, that was read from markdown static file"""
    markdown_name = None  # filename must be provided

    def get_context_data(self, **kwargs):
        if self.markdown_name is None:
            raise ImproperlyConfigured(
                "MarkdownTemplateView requires a definition of 'markdown_name'"
            )

        context = super().get_context_data(**kwargs)
        md = settings.BASE_DIR / settings.STATIC_ROOT / 'md' / self.markdown_name
        with md.open('r') as f:
            context['text'] = f.read()
        return context


class HomeView(MarkdownTemplateView):
    template_name = "home.html"
    markdown_name = 'homepage.md'


class AboutView(MarkdownTemplateView):
    template_name = "about.html"
    markdown_name = 'about.md'


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
        context['exercises'] = Exercise.objects.filter(tutorial=self.object)
        return context


class TutorialsView(ListView):
    model = Tutorial
    template_name = "tutorial_list.html"


class CSSExampleView(TemplateView):
    template_name = "mini-css-usage-example.html"


class SolutionView(LoginRequiredMixin, FormView):
    form_class = FileFieldModelForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
