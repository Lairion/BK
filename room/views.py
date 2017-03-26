from django.shortcuts import render
from .models import Room
# Create your views here.
def show_rooms(request):
	rooms = Room.objects.all()
	print(rooms) 
	context = {
		"rooms": rooms
	}
	return render(request,"main_menu.html",context)
def create_players(request):
	context = {
		"title":"Create players"	
	}
	return render(request,"characters_create.html", context)
