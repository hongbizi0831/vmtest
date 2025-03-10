import json

with open('favorite.json') as fo:
	print(json.load(fo))