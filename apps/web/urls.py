from django.urls import path

from .views import (
    HomeView,
    LearnView,
    AboutView
)

urlpatterns = [
    path('', HomeView.as_view()),
    path('learn/', LearnView.as_view()),
    path('about/', AboutView.as_view()),
]
