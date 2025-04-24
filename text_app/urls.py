from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/<str:text>/', views.result, name='result'),
] 