from name_function import get_formatted_name

"""
从用户输入接收名和姓，调用get_formatted_name并返回格式化名字，最后输出
"""
print("Enter 'q' to quit.")
while True:
	first = input("input first name: ")
	if first =='q':
		break
	last =  input("input last name: ")
	if last =='q':
		break

	full_name=get_formatted_name(first,last)
	print("\tfull name: "+full_name)