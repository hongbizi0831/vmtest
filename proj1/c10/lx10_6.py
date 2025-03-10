print("请输入加法运算的2个整数数字：")
n1 = input("请输入第一个数字：")
n2 = input("请输入第二个数字：")
try:
	sum = int(n1) + int(n2)
except ValueError:
	print("输入的不是2个整数，不能进行整数加法运算")
else:
	print(n1 + " + " + n2 + " = " + str(sum))