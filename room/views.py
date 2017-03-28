from django.shortcuts import render
from .models import Room,Character
# Create your views here.
def show_rooms(request):
	rooms = Room.objects.all()
	characters = Character.objects.all()
	context = {
		"title":"Rooms",
		"rooms": rooms,
		"characters":characters
	}
	return render(request,"main_menu.html",context)
def create_players(request):
	context = {
		"title":"Create players"	
	}
	return render(request,"characters_create.html", context)
def create_room(request):
	if request.method == "GET":
		name_room = request.GET.get("nameRoom")
		name_player = request.GET.get("nameChar")
		race_player = request.GET.get("raceChar")
		name_enemy = request.GET.get("nameEnem")
		race_enemy = request.GET.get("raceEnem")
		print(name_room)
		room = Room(name=name_room,game_type = "SP")
		room.save()
		players = Character(room=room, name = name_player, race =race_player)
		enemy = Character(room=room, name = name_enemy, race =race_enemy)
		players.save()
		enemy.save()
		return show_rooms(request)
