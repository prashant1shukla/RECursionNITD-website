from django.db import models


# Create your models here.

class Codeforces(models.Model):
    username = models.CharField(max_length=64, unique=True, db_index=True)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    current_rating = models.PositiveIntegerField(default=0)
    max_rating = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}({},{})".format(self.first_name, self.last_name, self.current_rating, self.is_active)

    class Meta:
        verbose_name_plural = 'Codeforces'
        ordering = ('-is_active', '-current_rating')
