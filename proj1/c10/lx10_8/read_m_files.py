def read_file(file_name):
	try:
		with open(file_name) as file_object:
			lines = file_object.readlines()
	except FileNotFoundError:
		# print("The file '" + file_name + "' does not exist.")
		pass
	else:
		print("The file '" + file_name + "' contains following info:")
		for line in lines:
			print(line.strip())

file_list = ['cats.txt','pandas.txt','dogs.txt']
for file in file_list:
	read_file(file)