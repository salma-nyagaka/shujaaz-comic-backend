from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)

    username = models.CharField(max_length=256,
                             blank=True,
                             default='Regular User')
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=256, blank=True)
    avatar = models.CharField(max_length=256, blank=True)

    @staticmethod
    def get_user_by_id(user_id):
        user = User.objects.get(id=user_id)
        return user
