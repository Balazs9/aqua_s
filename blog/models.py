from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Drafts"), (1, "Published"))


class Feedback(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    posted_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='bloglike', blank=True)

    class Meta:
        ordering: ['posted_date']

    def __str__(self):
        return self.title

    def item_like(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    chatbox = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering['posted_date']

    def __str__(self):
        return f'{self.name} commented {self.chatbox}.'