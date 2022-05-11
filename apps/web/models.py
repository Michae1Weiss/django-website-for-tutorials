from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


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
