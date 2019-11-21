from django.db import models
from .Enum import Kind, Tag
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

# add
from .discriminator_xception import Discriminator as Dscriminator


class CustomUser(AbstractUser):
    password = models.CharField(_('password'), max_length=128, validators=[MinLengthValidator(8)])
    email = models.EmailField(unique=True)


class Image(models.Model):
    file = models.FileField(blank=False, null=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    viewable = models.BooleanField()
    checked = models.BooleanField(default=False)
    # #TODO tagをゆず、キタ、イワを表すEnum型に変更
    tag = models.CharField(max_length=4, choices=Tag.choices(), null=True)
    description = models.TextField(max_length=360, null=True)
    # add
    yuzu_mean = [0.473011202617427, 0.4782059758651597, 0.507979008834504]
    yuzu_std = [0.2559886470196603, 0.2586286530046429, 0.271950605656863]

    discriminator_yuzu = Dscriminator('/api/model/yuzu/xception.pth', yuzu_mean, yuzu_std)


    def __str__(self):
        return self.file.name

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
            commenters.append(comment.commenter)
        return commenters

    def list_of_empathizer(self):
        empathys = Empathy.objects.filter(image=self)
        empathizers = []
        for empathy in empathys:
            empathizers.append(empathy.empathizer)
        return empathizers

    # 追加
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        yuzu_result = self.discriminator_yuzu.predict(self.file)
        self.viewable = True
        if yuzu_result == 0:
            self.tag = "IWA"
        elif yuzu_result == 1:
            self.tag = "KITA"
        elif yuzu_result == 2:
            self.tag = "OTHER"
            self.viewable = False
        else:
            self.tag = "YUZU"

        super(Image, self).save()
    def update(self):
        print("change")
        self.checked = True
        super(Image, self).save()


class Empathy(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    empathizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    # TODO:kindはいいね等を表すenum型に変更
    kind = models.CharField(max_length=10, choices=Kind.choices())

    class Meta:
        unique_together = (('image', 'empathizer'),)
        index_together = (('image', 'empathizer'),)


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    commenter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=360)

    class Meta:
        unique_together = (('image', 'commenter'),)
        index_together = (('image', 'commenter'),)


