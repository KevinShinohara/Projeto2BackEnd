from django.urls import path

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    path('api/nota', views.api_movie),
    path('api/movie/<int:movie_id>/', views.api_movie),
]