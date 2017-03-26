from django.db import models

# Create your models here.
class Room(models.Model):
	GAME_TYPES = (("SP","Simpleplay"),("MP","Multiplay"))
	name = models.CharField(max_length = 50)
	game_type = models.CharField(max_length = 3, choices = GAME_TYPES) 
	data_begin = models.DateField(auto_now = True)
	data_end = models.DateField(blank = True)

class Character:
	BODY_PARTS = ["Head","Torso","Left hand","Right hand","Legs"]
	health = 100
	health_shield = 100
	state = False

	def __init__ (self, name, race):
		self.name = name
		self.race = race
	
	def hit(self,target):
		if target == 0:
			self.health -= 50
		elif target == 1:
			self.health -= 40
		elif 2 <= target <= 3:
			self.health -= 10
		elif target == 4:
			self.health -= 20 
	def attack(self,enemy):
		print(enemy.block_part)
		if self.target != enemy.block_part:
			enemy.hit(self.target)
	def choice_target(self, target):
		self.target = target
	def body_block(self,block_part):
		self.block_part = block_part	