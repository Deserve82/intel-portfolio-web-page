from django.contrib import admin
from django.urls import path
from projects.views import main, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<str:username>', main),
    path('', home)
]
