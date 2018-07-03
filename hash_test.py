import unittest
from hash import Hash

class HashTests(unittest.TestCase):
	def test_put_method(self):
		testHash = Hash()
		testHash.put('foo', 'this is a thing')
		self.assertTrue(testHash.hashTable[3] == 'this is a thing')

	def test_get_method(self):
		testHash = Hash()
		testHash.put('foo','this is a thing')
		testGet = testHash.get('foo')
		self.assertTrue(testGet == 'this is a thing')

	def test_throw_exception_for_collisions(self):
		testHash = Hash()
		testHash.put('foo', 'this is a thing')
		with self.assertRaises(Exception):
			testHash.put('foo', 'a new thing')

if __name__ == '__main__':
	unittest.main()
