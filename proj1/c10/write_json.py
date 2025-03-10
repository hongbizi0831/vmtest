import json

number_list = [2,3,5,7,16,25]

with open('write_json_file.json','w') as file_object:
	json.dump(number_list,file_object)