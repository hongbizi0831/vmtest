from collections import OrderedDict

word_list = OrderedDict()
word_list['keai']='girl'
word_list['aa']='aaa'
word_list['ss']='bb'

for key,value in word_list.items():
	print(key,value)