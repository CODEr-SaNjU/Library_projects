from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.fields.related import ForeignKey
from .managers import UserManager
from django.utils import timezone, tree
from django.core.validators import RegexValidator


class UserProfile(AbstractBaseUser, PermissionsMixin):
    Email = models.EmailField(
        "Email Address",
        max_length=255,
        unique=True,
        error_messages={'unique': ("A user with that Email address already exists")})

    phone_regex = RegexValidator(regex=r"^(?:[0-9]●?){6,14}[0-9]$", message=(
        "Enter a valid international mobile phone number starting with +(country code)"))

    Mob_Number = models.CharField(
        "Phone Number ",
        validators=[phone_regex],
        max_length=20,
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


class BookAdd(models.Model):
    Book_Name = models.CharField("Books Name", max_length=50)

    def __str__(self):
        return self.Book_Name


class BookPublication(models.Model):
    Book_Publication = models.CharField("Book Publication", max_length=250)

    def __str__(self):
        return self.Book_Publication


class BookAuthor(models.Model):
    Book_Name = models.ForeignKey(
        BookAdd, verbose_name="Books Name", on_delete=models.CASCADE)
    Book_Author = models.CharField("Book Authors Name ", max_length=200)

    def __str__(self):
        return self.Book_Author


class BookCategory(models.Model):
    Book_Category = models.CharField("Book Category ", max_length=150)

    def __str__(self):
        return self.Book_Category


class BookCode(models.Model):
    Book_Ifsc = models.CharField(
        "Book Ifsc Number", max_length=13,)

    def __str__(self):
        return self.Book_Ifsc


STATUS = (
    (0, "Yes"),
    (1, "No")
)


class Bookinfo(models.Model):
    Book_Name = models.ForeignKey(
        BookAdd, verbose_name="Book Name", on_delete=models.CASCADE)
    Book_Author = models.ForeignKey(
        BookAuthor, verbose_name="Book Author Name ", on_delete=models.CASCADE)
    Book_Category = models.ForeignKey(
        BookCategory, verbose_name="Book Category Type", on_delete=models.CASCADE)
    Book_Ifsc = models.ForeignKey(
        BookCode, verbose_name="Book Ifsc Number", on_delete=models.CASCADE)
    Issued_Date = models.DateField(
        "Issued Date", auto_now=False, auto_now_add=False)
    Availability_Status = models.IntegerField(
        "Availability Status", choices=STATUS, default=1)
    Book_Publication = models.ForeignKey(
        BookPublication, verbose_name="Book Publication", on_delete=models.CASCADE)

    def __str__(self):
        return self.Book_Name.__str__()
