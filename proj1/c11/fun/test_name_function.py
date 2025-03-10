import unittest

from name_function import get_formatted_name

class TestNameFunction(unittest.TestCase):
	def test_first_last_name(self):
		full_name=get_formatted_name('john','smith')
		self.assertEqual(full_name,"John Smith")

	def test_first_middle_last_name(self):
		full_name=get_formatted_name('john','smith','tim')
		self.assertEqual(full_name,"John Tim Smith")

if __name__ == '__main__':
    unittest.main()