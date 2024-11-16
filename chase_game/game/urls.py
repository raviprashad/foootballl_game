from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('', views.game_view, name='game_interface'),
]


