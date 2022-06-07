from django import forms

from .models import ExerciseSolution


class FileFieldModelForm(forms.ModelForm):

    class Meta:
        model = ExerciseSolution
        fields = ['user_solution', 'exercise']
