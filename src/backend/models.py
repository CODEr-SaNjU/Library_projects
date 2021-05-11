from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import StudentProfileManager


class StudentProfile(AbstractBaseUser):
    Email = models.EmailField("Email Address", max_length=300, unique=True)
    MobNumber = models.CharField("Phone Number ", max_length=15, unique=True)
    StudentId = models.CharField(
        "Student Id Number", unique=True, max_length=100)
    FullName = models.CharField("Full Name", max_length=300)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    ProfilePhoto = models.ImageField(
        upload_to='photos/', null=True, blank=True)

    objects = StudentProfileManager()

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('Student Profile')
        verbose_name_plural = ('Student Profile')

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        send email to this user
        '''
        send_mail(subject, message, from_email, [self.Email], **kwargs)
