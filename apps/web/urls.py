from django.urls import path

from .views import (
    HomeView,
    AboutView,
    TutorialView,
    TutorialsView,
    CSSExampleView,
    SolutionView
)

urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view()),
    path('tutorial/day-<int:day>/', TutorialView.as_view()),
    path('tutorials/', TutorialsView.as_view()),
    path('mini-css/', CSSExampleView.as_view()),
    path('upload-solution/<int:id>/', SolutionView.as_view()),
]



