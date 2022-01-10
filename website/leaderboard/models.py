from django.db import models


# Create your models here.
class StopStalk(models.Model):
    username = models.CharField(max_length=200, unique=True)
    stopStalk_id = models.PositiveIntegerField(unique=True)
    codechef_url = models.URLField(blank=True)
    codeforces_url = models.URLField(blank=True)
    spoj_url = models.URLField(blank=True)
    codechef_solved = models.PositiveIntegerField(default=0)
    codeforces_solved = models.PositiveIntegerField(default=0)
    spoj_solved = models.PositiveIntegerField(default=0)
    total_solved = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['username', ]
        verbose_name_plural = 'StopStalkProfiles'
