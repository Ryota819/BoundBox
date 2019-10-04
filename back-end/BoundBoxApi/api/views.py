from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .models import Image, Comment, Empathy
from .serializers import UserSerializer, ImageSerializer, CommentSerializer, EmpathySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class EmpathyViewSet(viewsets.ModelViewSet):
    queryset = Empathy.objects.all()
    serializer_class = EmpathySerializer