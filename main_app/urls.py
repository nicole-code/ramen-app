from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginuser, name='login'),
    path('userprofile/', views.userprofile, name='user'),
    path('accounts/signup/', views.signup, name='signup'),
    path('buildramen/', views.buildramen, name='buildramen'),
]