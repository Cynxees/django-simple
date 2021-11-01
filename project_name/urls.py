from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.Homepage.as_view(),name='homepage'),
    path('admin/', admin.site.urls),
]
