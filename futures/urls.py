from django.urls import path
from futures import views

app_name = 'futures'

urlpatterns = [
    path('', views.main, name='main'),
]