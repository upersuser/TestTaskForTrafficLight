from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)

class Post(models.Model):
    user_id = models.IntegerField()
    post_theme = models.CharField(max_length=1000)
    post_text = models.CharField(max_length=5000)

