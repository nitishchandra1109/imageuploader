from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('delete/<int:id>/', views.delete_img,name='delete_img'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
