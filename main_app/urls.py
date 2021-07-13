from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('userprofile/', views.user_profile, name='user'),
    path('buildramen/', views.build_ramen, name='build_ramen'),
    path('accounts/signup/', views.signup, name='signup'),

    # path('usereditprofile/', views.edit_profile, name='edit_profile'),
    # path('updateuser/<int:profile_id>/', views.user_update_form),


    path('buildramen/', views.buildramen, name='buildramen'),

]