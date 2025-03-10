file_path='learning_python.txt'

# with open(file_path) as file_object:
# 	contents = file_object.read()
# 	print(contents.rstrip())

# with open(file_path) as file_object:
# 	for line in file_object:
# 		print(line.rstrip())
#
with open(file_path) as file_object:
	lines = file_object.readlines()

for a in lines:
	print(a.rstrip())