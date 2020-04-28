from django.db import models
from shujaaz.apps.comic.models import comic


class Stories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, blank=True)
    paragraph = models.CharField(max_length=256, blank=True)
    comic = models.ForeignKey(comic, on_delete=models.CASCADE)
