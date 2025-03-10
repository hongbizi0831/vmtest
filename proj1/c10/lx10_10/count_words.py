def count_word_number(file_path,word):
	try:
		with open(file_path,encoding='utf-8') as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print("The file '"+file_path+"' does not exist.")
	else:
		word_list = contents.split()
		for i in range(len(word_list)):
			word_list[i]=word_list[i].lower()
		word_count = word_list.count(word)
		print("The file '"+file_path+"' has "+str(word_count) + " '"+word + "' in it.")

file_list = [r'txt_files\als.txt',r'txt_files\hlpt.txt',r'txt_files\xwz.txt']
for file in file_list:
	count_word_number(file,'it')