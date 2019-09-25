from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .Enum import Kind, Tag


class Image(models.Model):
    file = models.FileField(blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=datetime.now)
    viewable = models.BooleanField()
    #TODO tagをゆず、キタ、イワを表すEnum型に変更
    tag = models.CharField(max_length=2, choices=Tag.choices())
    description = models.TextField(max_length=360)

    def no_of_comments(self):
        comments = Comment.objects.filter(image=self)
        return len(comments)

    def no_of_empathy(self):
        empathys = Empathy.objects.filter(image=self)
        return len(empathys)

    def list_of_commenter(self):
        comments = Comment.objects.filter(image=self)
        commenters = []
        for comment in comments:
            commenters.add(comment.commenter)
        return commenters

    def list_of_empathizer(self):
        empathys = Empathy.objects.filter(image=self)
        empathizers = []
        for empathy in empathys:
            empathizers.add(empathy.commenter)
        return empathizers


class Empathy(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    empathizer = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO:kindはいいね等を表すenum型に変更
    kind = models.CharField(max_length=2, choices=Kind.choices())


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=360)



