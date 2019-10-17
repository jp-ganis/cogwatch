import string
import random

mining_stats = {}
mining_stats["salt"] = 10
mining_stats["cybrous"] = 4

def mine(v):
	v = mining_stats[v]
	return random.randint(0,v)

def generate_name():
	vowels = ["a","e","i","o","u","y"]
	consonants = [l for l in string.ascii_lowercase if l not in vowels]
	
	name = ""
	
	v = random.randint(0,1)
	for i in range(6):
		v = (v + 1) % 2
		
		if v == 0:
			name += random.choice(vowels)
		else:
			name += random.choice(consonants)
			
	return name

class Cog():
	def __init__(self):
		self.name = generate_name()
		self.i = {}
		self.i["salt"] = 10
		self.i["cybrous"] = 10
		self.i["dollars"] = 100
		self.i["faith"] = 10
		self.dead = False
	
	def mine(self, comm):
		m = mine(comm)
		self.i[comm] += m
		return m
		
	def live_day(self):
		if not self.dead:
			for comm in ["salt","cybrous","faith"]:
				if self.i[comm] < 1: self.die()
				self.i[comm] -= 1
		
	def trade(self, cog, terms):
		if self.dead or cog.dead: return False
		
		my_amount = terms[0]
		my_comm = terms[1]
		their_amount = terms[2]
		their_comm = terms[3]
		
		valid_deal = self.i[my_comm] >= my_amount and cog.i[their_comm] >= their_amount
		
		if valid_deal:
			self.i[my_comm] -= my_amount
			self.i[their_comm] += their_amount
			
			cog.i[my_comm] += my_amount
			cog.i[their_comm] -= their_amount
			
			print(self, cog, terms)
		return valid_deal
	
	def die(self):
		self.dead = True
		# print("\n",self.name,"died\n")
			
	def __str__(self):
		if self.dead: return "{}: DEAD".format(self.name)
		return "{}".format(self.name)
		
	def __repr__(self):
		return self.__str__()