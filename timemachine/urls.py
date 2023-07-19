from django.urls import path
from . import views

app_name = 'time_machine'

urlpatterns = [
    path('get-ready/', views.get_ready, name='get_ready'),
    path('time-travel/<str:option>/', views.time_travel, name='time_travel'),
]