from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app_name = 'posts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/enquiryform/', views.enquiryform,name = "enquiryform"),
]