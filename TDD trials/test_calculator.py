import unittest
from calculator import Calculator

class MyFirstTDD(unittest.TestCase):
	"""docstring for MyFirstTDD"""
	def test_calculator_addition(self):
		calc = Calculator()
		result = calc.add(2,2)
		self.assertEqual(4, result)
		pass
	"""if __name__ == '__main__':
		unittest.main()"""