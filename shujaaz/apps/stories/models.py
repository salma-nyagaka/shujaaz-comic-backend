from django.db import models
from shujaaz.apps.comic.models import Comic


class Stories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, blank=True)
    paragraph = models.CharField(max_length=256, blank=True)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)


class Characters(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True)
    story = models.ForeignKey(Stories, on_delete=models.CASCADE)
