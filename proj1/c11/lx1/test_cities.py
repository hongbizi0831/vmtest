import unittest

from city_functions import get_formated_city

class TestCityFunction(unittest.TestCase):
	def test_city_country(self):
		my_formatted = get_formated_city('santiago','chile')
		self.assertEqual(my_formatted,'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()