from django.db import models

class Prompt(models.Model):
    setting = models.CharField(max_length=500)
    author = models.CharField(max_length=25)

    def __str__(self):
        return self.setting

class Post(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=25)

