from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Image, Comment, Empathy ,CustomUser
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
from .discriminator_xception import Discriminator
from django.db import reset_queries

from urllib import parse

from django.utils.encoding import force_str


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    pagination_class = LimitOffsetPagination
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.data['owner'])
        file_serializer = ImageSerializer(data=request.data)
        # viewable = True
        if file_serializer.is_valid():
            file_serializer.save(owner=user)
            reset_queries()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        if "owner" in request.GET:
            get_data = request.query_params
            image = Image.objects.filter(owner=get_data['owner'], viewable='True').order_by('timestamp').reverse()
        else:
            image = Image.objects.filter(viewable='True').all().order_by('timestamp').reverse()

        if "checked" in request.GET:
            get_data = request.query_params
            image = Image.objects.filter(checked='False').all().order_by('timestamp').reverse()

        pagenator = LimitOffsetPagination()
        result_page = pagenator.paginate_queryset(image, request)
        serializer = ImageSerializer(result_page, many=True)
        response = {'message': 'get image', 'result': serializer.data, "next": remove_query_param(pagenator.get_next_link(),'')}
        reset_queries()
        return Response(response, status=status.HTTP_200_OK)

    def patch(self, request):
        image = Image.objects.get(pk=request.data['image'])
        tag = request.data['updateTag']
        if tag == 1:
            image.tag = "YUZU"
        if tag == 2:
            image.tag = "KITA"
        if tag == 3:
            image.tag = "IWA"
        if tag == 4:
            image.tag = "Other"
        print(image.tag)
        image.update()
        response = {'message': 'update image'}
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request):

        image = Image.objects.get(pk=request.query_params['file'])
        image.viewable = False
        image.save()
        response = {'message': 'delete image'}
        reset_queries()
        return Response(response, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    parser_class = (FileUploadParser,)
    serializer_class = CommentSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


class EmpathyViewSet(viewsets.ModelViewSet):
    queryset = Empathy.objects.all()
    serializer_class = EmpathySerializer
    pagination_class = LimitOffsetPagination
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def create(self, request):
        try:
            empathy = Empathy.objects.get(image_id=request.data['image'], empathizer_id=request.data['empathizer'])
            empathy.delete()
            response = {'message': 'delete'}
            reset_queries()
            return Response(response, status=status.HTTP_201_CREATED)
        except Empathy.DoesNotExist:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(image_id=request.data['image'], empathizer_id=request.data['empathizer'])
                reset_queries()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        if "empathizer" in request.GET:
            get_data = request.query_params
            empathies = Empathy.objects.filter(empathizer=get_data['empathizer']).order_by('timestamp').reverse()
        else:
            empathies = Empathy.objects.all().order_by('timestamp').reverse()

        pagenator = LimitOffsetPagination()
        result_page = pagenator.paginate_queryset(empathies, request)
        serializer = EmpathySerializer(result_page, many=True)
        response = {'message': 'get empathy', 'result': serializer.data, "next": remove_query_param(pagenator.get_next_link(),'')}
        reset_queries()

        return Response(response, status=status.HTTP_200_OK)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = CustomUser.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many=False)
        reset_queries()
        return Response({'token': token.key, 'user': serializer.data})

def remove_query_param(url, key):
    """
    Given a URL and a key/val pair, remove an item in the query
    parameters of the URL, and return the new URL.
    """
    (scheme, netloc, path, query, fragment) = parse.urlsplit(force_str(url))
    query_dict = parse.parse_qs(query, keep_blank_values=True)
    # query_dict.pop(key, None)
    scheme = ''
    netloc = ''
    query = parse.urlencode(sorted(list(query_dict.items())), doseq=True)
    return parse.urlunsplit((scheme, netloc, path, query, fragment))