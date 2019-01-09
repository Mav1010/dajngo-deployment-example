from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from basicapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('basicapp/', include('basicapp.urls')),
    path('logout/', views.user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

