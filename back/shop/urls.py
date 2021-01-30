from django.urls import include, path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('get/', GetTestAPI.as_view()),
]