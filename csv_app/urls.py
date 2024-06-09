from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_csv, name='upload_csv'),
    path('process/', views.process_csv, name='process_csv'),
]
