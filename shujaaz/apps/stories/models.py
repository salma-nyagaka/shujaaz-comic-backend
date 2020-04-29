from django.db import models
from shujaaz.apps.comic.models import Comic


class Stories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=3000, blank=True)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
