from django.conf.urls import url
from .views import (show_rooms,create_players)

urlpatterns = [
    url(r'^main/$', show_rooms ),
    url(r'^createplayers/$', create_players ),
]