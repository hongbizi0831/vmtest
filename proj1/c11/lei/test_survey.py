import unittest

from asurvey import AServer

class TestSurvey(unittest.TestCase):
	def setUp(self):
		question = "input one language: "
		self.my_survey = AServer(question)
		self.answer_list = ['aa', 'bb', 'cc']
		for al in self.answer_list:
			self.my_survey.append_answer(al)

	def test_survey_one_answer(self):
		self.assertIn(self.answer_list[0],self.my_survey.answer[0])

	def test_survey_three_answer(self):
		for al in self.answer_list:
			self.assertIn(al,self.my_survey.answer)

if __name__ == '__main__':
    unittest.main()