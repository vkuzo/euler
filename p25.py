"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

import math
import unittest

def firstFibDigGtr(n):
	"""
	Returns the counter of the first Fibonacci number with # digits greater than n
	"""
	f1 = 1
	f2 = 1
	counter = 2
	keepGoing = True
	while keepGoing:
		f1, f2 = f2, f1 + f2
		counter += 1
		if n < len(str(f2)):
			keepGoing = False
			break
	return counter

class testProblem(unittest.TestCase):
	def setUp(self):
		pass
		
	def testFirstFibDigGtr(self):
		self.assertEquals(7, firstFibDigGtr(1))
		self.assertEquals(12, firstFibDigGtr(2))
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print firstFibDigGtr(999)