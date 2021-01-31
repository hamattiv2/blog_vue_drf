from django.urls import include, path
from . import views

# app_name = 'shop'

urlpatterns = [
    path('get/', views.GetTestAPI.as_view(), name="test"),
]