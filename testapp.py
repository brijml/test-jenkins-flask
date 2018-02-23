from run import app
import unittest

class AppTest(unittest.TestCase):
	
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/')
		assert b"Hello World!" in response.data

if __name__ == '__main__':
	unittest.main()