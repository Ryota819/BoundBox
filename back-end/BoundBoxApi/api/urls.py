from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include, url
from .views import CustomObtainAuthToken, CommentViewSet, UserViewSet, EmpathyViewSet, FileUploadView

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'empathys', EmpathyViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^images/$', FileUploadView.as_view()),
    url(r'^auth/', CustomObtainAuthToken.as_view()),
]
urlpatterns += router.urls

