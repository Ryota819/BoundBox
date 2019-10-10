from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Image, Comment, Empathy
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                        'email': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ImageSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Image
        fields = ('id', 'file', 'owner', 'tag', 'viewable', 'no_of_comments', 'no_of_empathy', 'list_of_commenter', 'list_of_empathizer')


class CommentSerializer(serializers.ModelSerializer):
    commenter = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'image', 'commenter', 'comment')


class EmpathySerializer(serializers.ModelSerializer):
    empathizer = UserSerializer()

    class Meta:
        model = Empathy
        fields = ('id', 'image', 'empathizer', 'kind')
