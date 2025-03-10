from user import User
class Privileges():
	def __init__(self):
		self.privileges = ['can add post','can delete post','can ban user']

	def show_admin_privileges(self):
		print("The admin privileges are:")
		for p in self.privileges:
			print(p,end=",")

class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privilege_list  = Privileges()