from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Image, Comment, Empathy
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = {'id', 'username', 'password', 'email'}
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = {'file', 'owner', 'viewable', 'tag', 'description'}


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = {'image', 'commenter', 'comment'}


class EmpathySerializer(serializers.ModelSerializer):
    class Meta:
        model = Empathy
        fields = {'image', 'empathizer', 'kind'}
