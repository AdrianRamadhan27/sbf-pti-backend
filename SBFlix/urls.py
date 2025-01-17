from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieListView.as_view()),
    path('add_movie/', views.MovieCreateView.as_view()),
    path('<int:pk>/', views.MovieDestroyView.as_view()),
]