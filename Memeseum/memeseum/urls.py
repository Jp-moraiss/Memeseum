from django.contrib import admin
from django.urls import path, include
from memeseum_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('memeseum_app.urls')),
]
