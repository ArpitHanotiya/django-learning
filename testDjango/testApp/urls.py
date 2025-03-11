from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_testApp, name='all_testApp'),
]