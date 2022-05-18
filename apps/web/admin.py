from django.contrib import admin

from .models import Tutorial, Exercise, ExerciseSolution, SolutionComment


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'name')


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('tutorial', 'exercise', 'correct_solution')


@admin.register(ExerciseSolution)
class ExerciseSolutionAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'user', 'user_solution', 'status')


@admin.register(SolutionComment)
class SolutionCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'solution', 'fixed_solution')
