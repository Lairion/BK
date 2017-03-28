from django.conf.urls import url
from .views import (show_rooms,create_players,create_room)

urlpatterns = [
    url(r'^main/', show_rooms ),
    url(r'^createplayers/', create_players ),
    url(r'^create_room/', create_room ),
]