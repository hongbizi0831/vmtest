import json

try:
	with open('favorite.json') as fo:
		n = json.load(fo)
except:
	n = input("please input your favorite number: ")
	with open('favorite.json','w') as fo2:
		json.dump(n,fo2)
else:
	print("rumber your favorite number:" + n)
