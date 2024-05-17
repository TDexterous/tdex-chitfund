from django.db import models

# Create your models here.


class Songs(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    duration = models.FloatField()
    last_play = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'song'
