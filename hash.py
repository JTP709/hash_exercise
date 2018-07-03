class Hash():
	def __init__(self):
		self.hashTable = []
		for i in range(10):
			self.hashTable.append(None)

	def __hashing(self, key):
		return len(key) % 10

	def put(self, key, value):
		index = self.__hashing(key)
		if self.hashTable[index] == None:
			self.hashTable[index] = value
		else:
			raise Exception('Two keys have collided!.')

	def get(self, key):
		index = self.__hashing(key)
		return self.hashTable[index]
