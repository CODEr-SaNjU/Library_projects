from django.urls import path, include
from .views import (BookListApiview)

urlpatterns = [
    path('', BookListApiview.as_view()),

]
