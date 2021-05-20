from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Bookinfo, BookCode, BookAdd, BookAuthor, BookCategory, BookPublication


class BookInfoSerializer(serializers.ModelSerializer):
    # Bookinfos = serializers.StringRelatedField(many=True)

    class Meta:
        model = BookAdd
        fields = ('Book_Name',)
