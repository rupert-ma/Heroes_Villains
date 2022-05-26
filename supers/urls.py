from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.Supers_List.as_view()),
    path('<int:pk>/', views.Supers_Detail.as_view()),
    ]    