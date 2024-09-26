from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.login, name='login'), # main - login page
    path('home/', views.home, name='home'),
]