class Battery():
	def __init__(self,battery_size):
		self.battery_size = battery_size

	def show_battery_size(self):
		return self.battery_size
class ElecCar():
	def __init__(self,name,battery):
		self.name=name
		self.battery = Battery(battery)

my_ecar = ElecCar('tesla',60)
size = my_ecar.battery.show_battery_size()
print(size)