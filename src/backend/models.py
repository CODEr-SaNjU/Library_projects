from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.fields import EmailField
from .managers import UserManager
from django.utils import timezone
from django.core.validators import RegexValidator


class UserProfile(AbstractBaseUser, PermissionsMixin):
    Email = models.EmailField(
        "Email Address",
        max_length=255,
        unique=True,
        error_messages={'unique': ("A user with that Email address already exists")})

    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=(
        "Enter a valid international mobile phone number starting with +(country code)"))

    Mob_Number = models.CharField(
        "Phone Number ",
        validators=[phone_regex],
        max_length=15,
        unique=True,
        error_messages={'unique': (
            "A user with that Phone Number address already exists")},
        null=True, blank=True)
    Full_Name = models.CharField("Full Name", max_length=300)
    is_active = models.BooleanField(default=True)
    # a admin user; non super-user
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)  # a superuser
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    ProfilePhoto = models.ImageField(
        upload_to='photos/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['Mob_Number']

    class Meta:
        ordering = ['Email']
        verbose_name = ('User Profile')
        verbose_name_plural = ('Users Profile')

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        send email to this user
        '''
        send_mail(subject, message, from_email, [self.Email], **kwargs)
