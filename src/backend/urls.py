from django.db import router
from django.urls import path, include
from knox import views as knox_views
from .views import (BookListApiview, UserRegisterApi, UserLoginApi)

urlpatterns = [
    path('', BookListApiview.as_view()),
    path('user/register/', UserRegisterApi.as_view(), name="register_user"),
    path('user/login/', UserLoginApi.as_view(), name='login'),
    path('user/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('user/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]
