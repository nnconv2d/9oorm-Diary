from django.urls import path, include
from . import views
from .views import signup_view


app_name = "users"
urlpatterns = [
    path('', views.login_request, name='login'), # main - login page
    path('home/', views.home_request, name='home'),
    path('signup/', signup_view, name='signup'),
]