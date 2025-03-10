def count_words(file_name):
	try:
		with open(file_name) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print("The file '"+file_name+"' does not exist.")
	else:
		words = contents.split()
		word_number = len(words)
		print("The file '"+file_name+"' has "+str(word_number)+" words.")

file_list=['guest_book.txt','my_file.txt','guest.txt']
for file in file_list:
	count_words(file)