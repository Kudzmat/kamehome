from django.urls import path
from . import views

app_name = 'my_profile'

urlpatterns = [
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile_page, name='profile'),
    path('add-profile-image/', views.add_profile_pic, name='add_profile_pic'),
    path('update-profile-image/', views.update_profile_pic, name='update_profile_pic'),
    path('password/', views.change_password, name='change_password'),
]