from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Bookinfo, BookCode, BookAdd, BookAuthor, BookCategory, BookPublication
from .models import UserProfile


class BookInfoSerializer(serializers.ModelSerializer):
    # Bookinfos = serializers.StringRelatedField(many=True)

    class Meta:
        model = BookAdd
        fields = ('Book_Name',)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('Email', 'Mob_Number', 'Full_Name',
                  'password', 'ProfilePhoto')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            validated_data['Email'], validated_data['Mob_Number'], validated_data['Full_Name'], validated_data['password', validated_data['ProfilePhoto']])
        return user
