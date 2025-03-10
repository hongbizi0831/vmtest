def get_formatted_name(first,last,middle=''):
	"""
	接收输入的名和姓，以格式化的方式返回： 名 姓，且首字母大写
	:param first: 名
	:param last: 姓
	:return: 返回格式化的名字字符串
	"""
	if middle =='':
		full_name = first+" "+last
	else:
		full_name = first+" "+middle+" "+last
	return(full_name.title())