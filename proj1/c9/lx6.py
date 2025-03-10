class Restaurant():
	def __init__(self,name,type):
		self.name=name
		self.type = type

class IceCreamStand(Restaurant):
	def __init__(self,name,type,flavors):
		super().__init__(name,type)
		self.flavors = flavors

	def show_icecream(self):
		print(self.name)
		print(self.type)
		for f in self.flavors:
			print(f)

my_ic = IceCreamStand('name1','type1',['aa','bb','cc'])
my_ic.show_icecream()