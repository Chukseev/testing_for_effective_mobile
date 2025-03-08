# urls.py
from django.urls import path
from .views import main, success

app_name = 'mainapp'

urlpatterns = [
    path('', main, name='main'),
    path('success/', success, name='success'),
]
