from django.urls import path
from . import views
urlpatterns = [
     path('',views.index, name='index'),
     #path('news',views.news, name='news'),
     path("car/<car_id>/",views.car_piece, name='car_piece'),
     path("car/<car_id>/AddPiece", views.Add_piece,name='add_piece'),
     path("car/<car_id>/<piece_id>/Views",views.comments, name='comments'),
     path("car/<car_id>/<piece_id>/Views/create_comment",views.create_comments, name='create_comments'),
]