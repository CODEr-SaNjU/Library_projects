from django.conf.urls.static import static
import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from backend import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("backend.urls")),
    path('', include('frontend.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
