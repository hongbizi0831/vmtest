import unittest

from employees import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.my_employee = Employee('ann','hardware',20000)

	def test_give_default_raise(self):
		self.my_employee.give_raise()
		self.assertEqual(self.my_employee.annual_salary,25000)

	def test_give_custom_raise(self):
		self.my_employee.give_raise(8000)
		self.assertEqual(self.my_employee.annual_salary, 28000)

if __name__ == '__main__':
    unittest.main()