from django.db import models

class Prompt(models.Model):
    author = models.CharField(max_length=25)
    body = models.CharField(max_length=500)
    post_date = models.DateField.auto_now_add()

    def __str__(self):
        return self.body

class Post(models.Model):
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=25)
    body = models.TextField()
    post_date = models.DateField.auto_now_add()

    def __str__(self):
        return self.title

class Chapter(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='chapters')
    body = models.TextField()
    chapter = models.PositiveIntegerField()
    post_date = models.DateField.auto_now_add()

    def __str__(self):
        return self.body

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    user = models.CharField(max_length=25)
    post_date = models.DateField.auto_now_add()

    def __str__(self):
        return self.body