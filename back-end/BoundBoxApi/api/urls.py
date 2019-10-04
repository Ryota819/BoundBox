from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ImageViewSet, CommentViewSet, UserViewSet, EmpathyViewSet

router = routers.DefaultRouter()
router.register('images', ImageViewSet)
router.register('comments', CommentViewSet)
router.register('empathys', EmpathyViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

