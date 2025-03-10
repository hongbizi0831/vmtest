class User():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

	def get_full_name(self):
		full_name = self.first_name + " " + self.last_name
		return full_name.title()

class Admin(User):
	def __init__(self,first_name,last_name,privileges):
		super().__init__(first_name,last_name)
		self.privileges  = privileges

	def show_admin_privileges(self):
		print("The admin privileges are:")
		for p in self.privileges:
			print(p,end=",")

privileges = ['can add post','can delete post','can ban user']
admin_user = Admin('anna','hardware',privileges)
full_name = admin_user.get_full_name()
print(full_name)
admin_user.show_admin_privileges()