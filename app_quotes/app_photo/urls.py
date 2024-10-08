from django.urls import path, include

from . import views

app_name = 'app_photo'

urlpatterns = [
    path('', views.index, name='home')  # app_photo:home
]
