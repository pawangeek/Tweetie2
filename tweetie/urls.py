from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('logout/', views.logout),
    path('login/', views.login),
    path('auth/', views.auth, name='auth'),
    path('tweet/', views.list_tweets),
    path('analyze/', views.analysis),
    path('about/', views.about),
]
