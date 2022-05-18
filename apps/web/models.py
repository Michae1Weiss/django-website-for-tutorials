from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)


class Tutorial(BaseModel):
    day = models.IntegerField(unique=True, validators=[MinValueValidator(1)])
    name = models.CharField(max_length=100, null=False)
    text = models.TextField(blank=False)


class Exercise(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    exercise = models.TextField()
    correct_solution = models.FileField(upload_to='correct_solution/')


class ExerciseSolution(models.Model):
    UPLOADED = 'Uploaded'
    REVIEW = 'Review'
    ACCEPTED = 'Accepted'
    DECLINED = 'Declined'
    SOLUTION_CHOICES = [
        (UPLOADED, 'Uploaded'),
        (REVIEW, 'Review'),
        (ACCEPTED, 'Accepted'),
        (DECLINED, 'Declined'),
    ]

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_solution = models.FileField(upload_to='user_solution/')
    status = models.CharField(max_length=255, choices=SOLUTION_CHOICES, default=UPLOADED)


class SolutionComment(models.Model):
    comment = models.TextField()
    solution = models.ForeignKey(ExerciseSolution, on_delete=models.CASCADE)
    fixed_solution = models.FileField(upload_to='fixed_solution/', null=True)
