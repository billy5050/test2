from django.urls import path
from app import views

urlpatterns = [
    path('',views.IndexViews.as_view(),name='index')
]