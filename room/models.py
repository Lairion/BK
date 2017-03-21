from django.db import models

# Create your models here.
class Room(models.Model):
	GAME_TYPES = (("SP","Simpleplay"),("MP","Multiplay"))
	name = models.CharField(max_length = 50)
	game_type = models.CharField(max_length = 3, choices = GAME_TYPES) 
	data_begin = models.DateField(auto_now = True)
	data_end = models.DateField(blank = True)
	