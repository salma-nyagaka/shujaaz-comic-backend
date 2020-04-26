from django.db import models
from shujaaz.apps.comic.models import Comic


class Stories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, blank=True)
    paragraph = models.CharField(max_length=256, blank=True)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    @staticmethod
    def get_story_by_comic_id(story_id):
        story = Stories.objects.get(id=story_id)
        return story
