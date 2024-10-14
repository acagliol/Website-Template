from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('main/', admin.site.urls),
    path('', include('administration.urls')),
    path('', include('counselor.urls')),
    path("login/", include("login.urls")),
    path('admin/', admin.site.urls)
]
