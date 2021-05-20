from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, viewsets
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Bookinfo
from .serializers import BookInfoSerializer


class BookListApiview(generics.ListAPIView):
    """
    list of all book and create a new snippet
    """

    queryset = Bookinfo.objects.all()
    serializer_class = BookInfoSerializer
