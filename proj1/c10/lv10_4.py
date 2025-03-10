file_path = 'guest_book.txt'

while True:
	name = input("Please input your name(enter 'quit' to end): ")
	if name =='quit':
		break
	print("Hello. " + name + ".")

	with open(file_path,'a') as file_object:
		file_object.write(name + "\n")