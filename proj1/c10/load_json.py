import json

with open('write_json_file.json') as file_object:
	numbers=json.load(file_object)

print(numbers)