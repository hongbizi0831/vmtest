name = input("Please input your name: ")

file_path = 'guest.txt'

with open(file_path,'a') as file_object:
	file_object.write(name + "\n")

with open(file_path) as fo:
	name_list = fo.read()
	print(name_list)