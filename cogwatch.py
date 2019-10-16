import random

from cog import Cog
	
class Populous():
	Population = []
	
	
class Farmer(Cog):
	def __init__(self):
		Cog.__init__(self)
		self.name = "farmer "+self.name 
		
	def live_day(self):
		if self.i["salt"] < self.i["cybrous"]:
			self.mine("salt")
		else:
			self.mine("cybrous")
			
		Cog.live_day(self)
		
class Bouj(Cog):
	def __init__(self):
		Cog.__init__(self)
		self.name = "mr "+self.name 
		
	def live_day(self):
		## buy from richest
		for comm in ["salt", "cybrous"]:
			cog_max = max(Populous.Population, key=lambda c: c.i[comm])
			amount = 2
			
			terms = (1 * amount, "dollars", amount, comm)
			
			self.trade(cog_max, terms)
		
		## sell to poorest
		for comm in ["salt", "cybrous"]:
			cog_min = min(Populous.Population, key=lambda c: c.i[comm])
			amount = 1
			
			terms = (amount, comm, 1 * amount, "dollars")
			self.trade(cog_max, terms)
			
	
		Cog.live_day(self)
		
		
def episode():
	pop = Populous.Population

	for i in range(2):
		pop.append(Farmer())
	for i in range(1):
		pop.append(Bouj())
		
	
	church = Cog()
	church.name = "Church"
	
	for i in range(30):
		church.i["faith"] = 1000
		
		for cog in pop:
			cog.live_day()
			
			church.trade(cog, (1, "faith", int(cog.i["dollars"] * 0.1), "dollars"))
			
			for comm in ["salt","cybrous"]:
				if cog.i[comm] <= 1:
					church.trade(cog, (1, comm, 0, "dollars"))
		
		if all([cog.dead for cog in pop]):  break
	
		print()
		for c in pop:
			print(c, c.i)
		print(church, church.i)
		print()
		
episode()