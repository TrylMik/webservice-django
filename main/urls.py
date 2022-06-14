from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('questions/', views.questions, name='questions'),
    path('movies/', views.movies, name='movies'),
    path('photos/', views.photos, name='photos'),
    #path('spots/', views.spots, name='spots'),
    #path('spots/create', views.create_spots, name='create_spots'),
    path('spots/', Spots.as_view(), name="Spots"),
    path('spots/<int:pk>', SpotsDetails.as_view(), name='Spots-Post-Detail'),
    path('spots/<int:pk>/comment', AddCommentSpots.as_view(), name='spots-post-comment'),
    path('spots/add', AddSpots.as_view(), name="add-spots"),
    path('spots/delete/<int:pk>', DeleteSpot.as_view(), name="delete-spots"),


]