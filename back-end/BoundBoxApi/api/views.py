from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .models import Image, Comment, Empathy
from .serializers import UserSerializer, ImageSerializer, CommentSerializer, EmpathySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.pagination import LimitOffsetPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class ImageViewSet(viewsets.ModelViewSet):
#     parser_class = (FileUploadParser,)
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (AllowAny,)
#
#     @action(detail=True, methods=['POST'])
#     def upload_file(self, request, pk=None):
#         user = User.objects.get(id=request.user)
#         request.data.append('owner', user)
#         image_serializer = ImageSerializer(data=request.data)
#
#         if image_serializer.is_valid():
#             image_serializer.save()
#             return Response(image_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    pagination_class = LimitOffsetPagination

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.data['owner'])
        file_serializer = ImageSerializer(data=request.data)
        if file_serializer.is_valid():
            # TODO 分類ロジックでtagをつける。
            tag = "YUZU"
            file_serializer.save(owner=user, tag=tag)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        if "query_params" in request.GET:
            get_data = request.query_params
            image = Image.objects.filter(owner=get_data['owner'], viewable='True').order_by('timestamp').reverse()
        else:
            image = Image.objects.all().order_by('timestamp').reverse()

        pagenator = LimitOffsetPagination()
        result_page = pagenator.paginate_queryset(image, request)
        serializer = ImageSerializer(result_page, many=True)
        response = {'message': 'get image', 'result': serializer.data, "next": pagenator.get_next_link()}

        return Response(response, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    parser_class = (FileUploadParser,)
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class EmpathyViewSet(viewsets.ModelViewSet):
    queryset = Empathy.objects.all()
    serializer_class = EmpathySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many=False)
        return Response({'token': token.key, 'user': serializer.data})

