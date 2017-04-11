from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Room,Character
from .character import Character_Demo
import random
# Create your views here.
player = Character_Demo("Manul","Ork")
enemy = Character_Demo("Hulk","Ork")
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
def attack(request):
	global player,enemy 
	if request.is_ajax():
		part_enemy = request.GET.get("partEnemy")
		part_player = request.GET.get("partPlayer")
		print(part_player)
		print(part_enemy)
		enemy.choice_target(random.randint(0,4))
		enemy.body_block(random.randint(0,4))
		player.choice_target(int(part_enemy))
		player.body_block(int(part_player))
		enemy.attack(player)
		player.attack(enemy)
		context = {
			"healthEnemy": enemy.health,
			"healthPlayer": player.health
		}
		jsresp = JsonResponse(context)
		return HttpResponse(jsresp.content, content_type='text/html')
	
