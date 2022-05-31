from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.Super_Type_List.as_view()),
    path('<int:pk>/', views.Super_Type_Detail.as_view()),
    ]    