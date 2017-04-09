from django.conf.urls import url
from .views import (show_rooms,create_players,fight_room)

urlpatterns = [
    url(r'^main/$', show_rooms ),
    url(r'^createplayers/$', create_players ),
    url(r'^fight_room/$', fight_room ),

]