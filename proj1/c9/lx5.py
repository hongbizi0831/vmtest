class User():
	def __init__(self,first_name,last_name,login_attempts):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = login_attempts

	def increment_login_attempts(self,incre):
		self.login_attempts += incre

	def reset_login_attempts(self):
		self.login_attempts = 0
	def describe_user(self):
		print("The user name is: " +
			  self.first_name.title() + " " +self.last_name.title() + ".")

	def greet_user(self):
		full_name = self.first_name.title() + " " + self.last_name.title()
		print("Hello, " + full_name + ".")

user1 = User('anna','hardware',0)
user1.increment_login_attempts(1)
print(user1.login_attempts)
user1.increment_login_attempts(2)
print(user1.login_attempts)
user1.increment_login_attempts(3)
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)