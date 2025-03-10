import json

n_s= input("input your favorite number: ")

with open('favorite.json','w') as fo:
	json.dump(n_s,fo)


