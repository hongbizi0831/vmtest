class AServer():
	def __init__(self,question):
		self.question = question
		self.answer= []

	# def show_question(self):
	# 	print(self.question)

	def append_answer(self,a):
		self.answer.append(a)

	# def show_answers(self):
	# 	print("The result is:")
	# 	for item in self.answer:
	# 		print("- "+item)