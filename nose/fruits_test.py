import unittest
import fruits

class FruitsTest(unittest.TestCase):

	def test_orange_is_orange(self):
		orange = fruits.Orange()
		self.assertEquals("orange", orange.color())

	def test_banana_is_yellow(self):
		banana = fruits.Banana()
		self.assertEquals("yellow", banana.color())

if __name__ == "__main__":
    unittest.main()
