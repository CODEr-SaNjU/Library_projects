from datetime import date
from decimal import Context
from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.http import HttpResponse
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth import login
from .models import Bookinfo
from .serializers import BookInfoSerializer, UserProfileRegisterSerializer, UserProfileSerializer
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


class BookListApiview(generics.ListAPIView):
    """
    list of all book and create a new snippet
    """

    queryset = Bookinfo.objects.all()
    serializer_class = BookInfoSerializer


class UserRegisterApi(generics.GenericAPIView):
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserProfileSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserLoginApi(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(UserLoginApi, self).post(request, format=None)
