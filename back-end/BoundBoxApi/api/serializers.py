from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Image, Comment, Empathy, CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                        'email': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class ImageSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    list_of_empathizer = UserSerializer(read_only=True, many=True)
    list_of_commenter = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Image
        fields = ('id', 'file', 'owner', 'tag', 'viewable', 'no_of_comments', 'no_of_empathy', 'list_of_commenter', 'list_of_empathizer')


class CommentSerializer(serializers.ModelSerializer):
    commenter = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'image', 'commenter', 'comment')


class EmpathySerializer(serializers.ModelSerializer):
    empathizer = UserSerializer(read_only=True)
    image = ImageSerializer(read_only=True)

    class Meta:
        model = Empathy
        fields = ('id', 'image', 'empathizer', 'kind')

