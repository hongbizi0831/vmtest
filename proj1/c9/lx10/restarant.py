class Restaurant():
	def __init__(self,name,type):
		self.name=name
		self.type = type

	def show_info(self):
		print(self.name + ', '+self.type)