from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from webchat.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="Index"),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
