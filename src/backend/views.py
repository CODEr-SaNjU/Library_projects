from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Bookinfo
from .serializers import BookInfoSerializer


class BookListApiview(APIView):
    pass
