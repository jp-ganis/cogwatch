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
			amount = 6
			price_per_unit = 1
			
			terms = (price_per_unit * amount, "dollars", amount, comm)
			
			self.trade(cog_max, terms)
		
		## sell to poorest
		for comm in ["salt", "cybrous"]:
			cog_min = min(Populous.Population, key=lambda c: c.i[comm])
			amount = 2
			price_per_unit = 5
			
			terms = (amount, comm, price_per_unit * amount, "dollars")
			self.trade(cog_max, terms)
			
	
		Cog.live_day(self)
		
class Church(Cog):
	def __init__(self):
		Cog.__init__(self)
		self.name = "Church"

	def live_day(self):
		if self.dead: return
		
		self.i["faith"] = 1000
		
		for cog in Populous.Population:
			if cog.i["dollars"] >= 10:
				self.trade(cog, (4, "faith", int(cog.i["dollars"]*0.1), "dollars"))
			
			for comm in ["salt","cybrous"]:
				if cog.i[comm] <= 9:
					self.trade(cog, (8, comm, 0, "dollars"))
		
		poorest_cog = min([cog for cog in Populous.Population], key=lambda x: x.i["dollars"])
		self.trade(poorest_cog, (20, "dollars", 0, "dollars"))
		
		
		self.i["dollars"] -= 1
		
		if self.i["dollars"] <= 0: self.die()
	
		
		
def episode(debug=False):
	Populous.Population = []
	pop = Populous.Population
	
	if random.random() >= 0.5:
		fiu = Farmer()
		fiu.name = "farmer fiu"
	else:
		fiu = Bouj()
		fiu.name = "mr fiu"
		
	pop.append(fiu)
	
	for i in range(15):
		pop.append(Farmer())
	for i in range(5):
		pop.append(Bouj())
		
	church = Church()
	pop.append(church)
			
	for i in range(300):		
		if debug:
			print()
			for c in pop:
				print(c, c.i)
			print()
			
		for cog in pop:
			cog.live_day()
		
		if all([cog.dead for cog in pop]):  break

	return len([cog for cog in pop if not cog.dead])
		
		
print(episode(True))
		
# bn = []
# bs = 0
# iters = 1000
# for i in range(iters):
	# print(bs, i/iters, end="\r")
	# s, n = episode()
	
	# if s > bs:
		# bs = s
		# bn = n
		
# # print(episode(True))
# print(bs, bn)