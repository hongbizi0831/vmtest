class Restaurant():

	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def set_number_served(self,number):
		self.number_served=number

	def increment_number_served(self,incre):
		self.number_served+=incre

	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restaurant(self):
		print("营业中")

resturant = Restaurant('test','abc')
print(resturant.number_served)
resturant.number_served=10
print(resturant.number_served)
resturant.set_number_served(36)
print(resturant.number_served)
resturant.increment_number_served(5)
print(resturant.number_served)
