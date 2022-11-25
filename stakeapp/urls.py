from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('allblog', views.blog),
    path('contact', views.contact),
    path('inquiry', views.inquiry),

    path('blog/<str:name>', views.blogByName),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
