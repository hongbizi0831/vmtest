def get_number(message):
	while True:
		number1 = input(message)
		try:
			n1=int(number1)
		except ValueError:
			print("输入的不是数字，请重新输入：")
		else:
			return n1

n1=get_number("请输入第一个整数：")
n2=get_number("请输入第二个整数：")
sum = n1+n2
print(str(n1) + ' + ' + str(n2) + " = " + str(sum))