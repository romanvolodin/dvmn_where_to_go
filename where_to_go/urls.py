from django.contrib import admin
from django.urls import path
from places import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
]
