from django.conf.urls import url
from .views import show_rooms

urlpatterns = [
    url(r'^main/', show_rooms ),
]