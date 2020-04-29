from django.db import models
from shujaaz.apps.user.models import User


class Comic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, blank=True)
    avatar = models.CharField(max_length=2000, blank=True)
    summary = models.CharField(max_length=256, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    @staticmethod
    def get_comic_by_id(comic_id):
        comic = Comic.objects.get(id=comic_id)
        return comic


class Characters(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True)    
    avatar = models.CharField(max_length=2000, blank=True)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

