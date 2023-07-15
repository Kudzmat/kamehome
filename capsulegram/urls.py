from django.urls import path
from . import views

app_name = 'capsulegram'

urlpatterns = [
    path('timeline/', views.CapsulePosts.as_view(), name='posts_page'),
    path('upload-image/', views.UploadPic.as_view(), name='upload')
]