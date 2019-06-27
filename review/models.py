from django.db import models
from django.core import validators

# Create your models here.
class cinemareview(models.Model):
    nickname = models.CharField(
        max_length=50,
        verbose_name="ニックネーム",
    )

    review = models.TextField(
        verbose_name='レビュー',
        blank=True,
        null=True,
        max_length=1000,
    )

    rate = models.DecimalField(
    verbose_name='レート',
    max_digits=2,
    decimal_places=1,
    blank=True,
    null=True,
    default=0.0,
    )
    

    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="レビュー日時",
        )   