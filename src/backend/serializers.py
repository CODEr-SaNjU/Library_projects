from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Bookinfo, BookCode, BookAdd, BookAuthor, BookCategory, BookPublication


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookinfo
        fields = "__all__"
