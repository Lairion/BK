# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse

# Create your models here.
class Room(models.Model):
	GAME_TYPES = (("SP","Simpleplay"),("MP","Multiplay"))
	name = models.CharField(max_length = 50)
	game_type = models.CharField(max_length = 3, choices = GAME_TYPES) 
	data_begin = models.DateField(auto_now = True)
	data_end = models.DateField(blank = True,null=True)
	def __str__(self):
		return self.name
	# функция для перехода на страницу шаблон по имени шаблона в url. 
	# arena это namespace в FightClub/urls.py для include()
	# in_room это name в room/urls.py для url по game
	# kwargs={"id": self.id} это передача значения как часть адреса.
	def get_absolute_url(self):
		return reverse("arena:in_room", kwargs={"id": self.id})	

class Character(models.Model):
	RACE = (("HM","Human"),("EL","Elf"),("OR","Orc"),("DW","Dwarf"),("WR","Werewolf"))
	room = models.ForeignKey(Room)
	name = models.CharField(max_length = 50)
	race = models.CharField(max_length = 3, choices = RACE)
	BODY_PARTS = ["Head","Torso","Left hand","Right hand","Legs"]
	health = models.IntegerField(default=100)
	def __str__(self):
		return self.name

	def hit(self,target):
		health = self.health
		if target == 0:
			self.health -= 50
		elif target == 1:
			self.health-= 40
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
	