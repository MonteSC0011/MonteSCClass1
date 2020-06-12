import unittest



###############################################################################################
#This is where the Unit Test Goes for testing the functions. 

class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')


	def test_isupper(self):

		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):

		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		#Check that s.split fails when the seperator is not a string

		with self.assertRaises(TypeError): 
			s.split(2)

if __name__ == '__main__':
	unittest.main()


