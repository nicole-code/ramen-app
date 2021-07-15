from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('community/hub', views.hub, name='hub'),
    path('community/community/<int:ramen_id>/', views.communitydetail, name= 'communitydetail'),
    path('login/', views.login_user, name='login'),
    path('userprofile/', views.user_profile, name='user'),
    path('userprofile/<int:ramen_id>/', views.user_ramen_detail, name= 'userdetail'),
    path('buildramen/<int:ramen_id>/edit/', views.user_ramen_edit, name='ramenedit'),
    path('edit/<int:ramen_id>', views.user_ramen_update, name='ramenupdate'),
    path('buildramen/new', views.buildramen_new, name='buildramen_new'),
    path('accounts/signup/', views.signup, name='signup'),
    path('post/', views.buildramen_create, name='buildramen_create' ),
    # path('buildramen/<int:ramen_id>/assoc_ingredient/<int:ingredient_id>/', views.assoc_ingredient, name='assoc_ingredient'),
    path('buildramen/<int:ramen_id>/delete/', views.ramen_delete, name='ramendelete'),
    path('userprofile/<int:ramen_id>/delete/', views.user_ramen_delete, name='user_ramen_delete')

]