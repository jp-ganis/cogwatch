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
	numbers = []
	
	def __init__(self):
		Cog.__init__(self)
		self.name = "mr "+self.name 
		
	def live_day(self):
		## buy from richest
		for comm in ["salt", "cybrous"]:
			cog_max = max(Populous.Population, key=lambda c: c.i[comm])
			amount = Bouj.numbers[0]
			price_per_unit = Bouj.numbers[1]
			
			terms = (price_per_unit * amount, "dollars", amount, comm)
			
			self.trade(cog_max, terms)
		
		## sell to poorest
		for comm in ["salt", "cybrous"]:
			cog_min = min(Populous.Population, key=lambda c: c.i[comm])
			amount = Bouj.numbers[2]
			price_per_unit = Bouj.numbers[3]
			
			terms = (amount, comm, price_per_unit * amount, "dollars")
			self.trade(cog_max, terms)
			
	
		Cog.live_day(self)
		
		
def episode(debug=False):
	Populous.Population = []
	pop = Populous.Population
	
	numbers = [random.randint(0,10) for _ in range(8)]
	numbers = [6, 1, 2, 5, 4, 0, 9, 8]
	Bouj.numbers = numbers

	for i in range(15):
		pop.append(Farmer())
	for i in range(5):
		pop.append(Bouj())
		
	
	church = Cog()
	church.name = "Church"
	
	for i in range(300):
		church.i["faith"] = 1000
		
		for cog in pop:
			cog.live_day()
			
			church.trade(cog, (numbers[4], "faith", 1+numbers[5], "dollars"))
			
			for comm in ["salt","cybrous"]:
				if cog.i[comm] <= numbers[6]:
					church.trade(cog, (numbers[7], comm, 0, "dollars"))
		
		if all([cog.dead for cog in pop]):  break

		if debug:
			print()
			for c in pop:
				print(c, c.i)
			print(church, church.i)
			print()
		
	return len([cog for cog in pop if not cog.dead]), numbers
		
		
# print(episode(True))
		
bn = []
bs = 0
iters = 1000
for i in range(iters):
	print(bs, i/iters, end="\r")
	s, n = episode()
	
	if s > bs:
		bs = s
		bn = n
		
# print(episode(True))
print(bs, bn)