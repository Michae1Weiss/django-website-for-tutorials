from django.urls import path

from .views import (
    HomeView,
    LearnView,
    AboutView,
    TutorialView,
    TutorialsView,
    CSSExampleView,
)

urlpatterns = [
    path('', HomeView.as_view()),
    path('learn/', LearnView.as_view()),
    path('about/', AboutView.as_view()),
    path('tutorial/day-<int:day>/', TutorialView.as_view()),
    path('tutorials/', TutorialsView.as_view()),
    path('mini-css/', CSSExampleView.as_view()),
]



