from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('community/<int:ramen_id>/', views.communitydetail, name= 'communitydetail'),
    path('login/', views.login_user, name='login'),
    path('userprofile/', views.user_profile, name='user'),
    path('buildramen/new', views.buildramen_new, name='buildramen_new'),
    path('accounts/signup/', views.signup, name='signup'),
    path('post/', views.buildramen_create, name='buildramen_create' ),
    path('buildramen/<int:ramen_id>/', views.ramendetail, name= 'ramendetail'),
    path('buildramen/<int:ramen_id>/delete/', views.ramen_delete, name='ramendelete'),
    # path('usereditprofile/', views.edit_profile, name='edit_profile'),
    # path('updateuser/<int:profile_id>/', views.user_update_form),

]