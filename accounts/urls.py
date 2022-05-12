from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import CreateStudentAPI, RegisterAPI, LoginAPI, UserAPI

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
    path('auth/register_new', CreateStudentAPI.as_view())
]