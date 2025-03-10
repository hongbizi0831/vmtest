import unittest

from city_functions import get_formatted_city

class TestCityFunction(unittest.TestCase):
	def test_city_country(self):
		my_formatted = get_formatted_city('santiago','chile')
		self.assertEqual(my_formatted,'Santiago, Chile - Population 0')

	def test_city_country_population(self):
		my_formatted = get_formatted_city('santiago', 'chile',population=5000000)
		self.assertEqual(my_formatted, 'Santiago, Chile - Population 5000000')

if __name__ == '__main__':
    unittest.main()