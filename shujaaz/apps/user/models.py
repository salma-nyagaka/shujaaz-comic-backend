from django.db import models
from django.contrib.sites.models import Site



class User(models.Model):
    sites = models.ManyToManyField(Site)
    id = models.AutoField(primary_key=True)

    username = models.CharField(max_length=256,
                             blank=True,
                             default='Regular User')
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=256, blank=True)

    @staticmethod
    def get_user_by_id(user_id):
        user = User.objects.get(id=user_id)
        return user
