from django.db import models
from .Enum import Kind, Tag
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

# add
from .discriminator_xception import Discriminator as xcepDscriminator
from .discriminator_resnet import Discriminator as resDiscriminator


class CustomUser(AbstractUser):
    password = models.CharField(_('password'), max_length=128, validators=[MinLengthValidator(8)])
    email = models.EmailField(unique=True)


class Image(models.Model):
    file = models.FileField(blank=False, null=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    viewable = models.BooleanField()
    checked = models.BooleanField(default=False)
    # add
    kita_mean = [0.49297256026361114, 0.4974875424166868, 0.5249390878377942]
    kita_std = [0.26663833485005356, 0.2701370696494548, 0.2788614149839678]
    iwa_mean = [0.45697290401600527, 0.46483589818332716, 0.49824474234682764]
    iwa_std = [0.25909249960699154, 0.2629111357014475, 0.2727926945783674]
    discriminator_kita = xcepDscriminator('/api/model/kitagawa/xception.pth', kita_mean, kita_std)
    discriminator_iwa = xcepDscriminator('/api/model/iwasawa/xception.pth', iwa_mean, iwa_std)


    def __str__(self):
        return self.file.name

    # #TODO tagをゆず、キタ、イワを表すEnum型に変更
    tag = models.CharField(max_length=4, choices=Tag.choices(), null=True)
    description = models.TextField(max_length=360, null=True)

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
        kita_result = self.discriminator_kita.predict(self.file)
        iwa_result = self.discriminator_iwa.predict(self.file)
        self.viewable = True
        if (kita_result == True and iwa_result == True):
            self.tag = "YUZU"
        elif (kita_result == True and iwa_result == False):
            self.tag = "KITA"
        elif (kita_result == False and iwa_result == True):
            self.tag = "IWA"
        else:
            self.tag = "OTHER"
            self.viewable = False

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


