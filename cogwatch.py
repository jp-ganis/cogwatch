import random
import string

## can mine salt
## need to eat 1 salt per day to survive
## can buy/sell salt

def mine(v):
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
		self.inventory = {}
		self.inventory["salt"] = 10
		self.inventory["cybrous"] = 10
		self.inventory["dollars"] = 10
		self.inventory["faith"] = 10
		self.dead = False
	
	def mine(self, comm, v):
		m = mine(v)
		self.inventory[comm] += m
		return m
		
	def live_day(self):
		if not self.dead:
			for comm in ["salt","cybrous","faith"]:
				if self.inventory[comm] < 1: self.die()
				self.inventory[comm] -= 1
	
	def die(self):
		self.dead = True
		print("\n",self.name,"died\n")
		
	def trade(self, cog, my_deal, their_deal):
		if self.dead or cog.dead: return False
		
		my_amount = my_deal[0]
		my_comm = my_deal[1]
		their_amount = their_deal[0]
		their_comm = their_deal[1]
		
		valid_deal = self.inventory[my_comm] >= my_amount and cog.inventory[their_comm] >= their_amount
		
		if valid_deal:
			self.inventory[my_comm] -= my_amount
			self.inventory[their_comm] += their_amount
			
			cog.inventory[my_comm] += my_amount
			cog.inventory[their_comm] -= their_amount
			
		return valid_deal
			
	def __str__(self):
		if self.dead: return "{}: DEAD".format(self.name)
		return "{} {}".format(self.name, str(self.inventory))
		
	def __repr__(self):
		return self.__str__()
		
		
def episode():
	c = Cog()
	d = Cog()
	e = Cog()
	
	pop = [c,d,e]
	
	d.dollars = 20
	
	church = Cog()
	church.name = "Church"
	
	for i in range(300):
		church.inventory["faith"] = 1000
		
		for cog in pop:
			for comm in ["salt","cybrous"]:
				if cog.inventory[comm] < 1:
					church.trade(cog, (1, comm), (0, "dollars"))
				church.trade(cog, (1, "faith"), (int(cog.inventory["dollars"] * 0.1), "dollars"))
			cog.live_day()
		
		if all([cog.dead for cog in pop]):  break
	
		
		m = c.mine("salt",16)
		y = e.mine("cybrous",16)
		
		m_tax = int(m*0.1)
		y_tax = int(y*0.1)
		
		## church taxes 10% of everything mined in order to help people who are starving
		church.trade(c, (0, "dollars"), (m_tax, "salt"))
		church.trade(e, (0, "dollars"), (y_tax, "cybrous"))
		
		d.trade(c, (2, "dollars"), (m-m_tax-1, "salt"))
		d.trade(e, (2, "dollars"), (y-y_tax-1, "cybrous"))
		
		d.trade(c, (1, "cybrous"), (3, "dollars"))
		d.trade(e, (1, "salt"), (3, "dollars"))
		
		
		print(c,"||",d,"||",e)
	print(church)
		
episode()