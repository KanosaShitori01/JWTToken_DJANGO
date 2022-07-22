from django.urls import path
from .views import RenderHome

urlpatterns = [
    path("", RenderHome.as_view(), name="home")
]