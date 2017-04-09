from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .models import Room,Character
# Create your views here.
@csrf_protect
def show_rooms(request):
	if request.method == "POST":
		name_room = request.POST.get("nameRoom")
		name_player = request.POST.get("nameChar")
		race_player = request.POST.get("raceChar")
		name_enemy = request.POST.get("nameEnem")
		race_enemy = request.POST.get("raceEnem")
		room = Room(name=name_room,game_type = "SP")
		room.save()
		players = Character(room=room, name = name_player, race =race_player)
		enemy = Character(room=room, name = name_enemy, race =race_enemy)
		players.save()
		enemy.save()
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
		"title":"Create players",
		"races":Character.RACE	
	}
	return render(request,"characters_create.html", context)
def fight_room(request):
	context = {"title":"Fight room"}
	return render(request,"fight_room.html", context)
	
