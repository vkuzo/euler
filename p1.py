"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import unittest

def sumOfConsInts(n):
	"""
	Retuns sum of consecutive integers from 1 to n
	"""
	return n * (n + 1) / 2

def sumOfMultiples(upper_bound, m1, m2):
	"""
	Returns the sum of multiples of m1 and m2 below upper_bound
	"""
	s = 0
	#add sums of each multiple
	s += m1 * sumOfConsInts((upper_bound-1) / m1) 
	s += m2 * sumOfConsInts((upper_bound-1) / m2) 
	#subtract sums of both multiples to avoid double counting
	s -= m1 * m2 * sumOfConsInts((upper_bound-1) / m1 / m2)
	return s

class testProblem(unittest.TestCase):	
	def setUp(self):
		pass
		
	def testSumOfConsInts(self):
		self.assertEqual(6, sumOfConsInts(3))
		self.assertEqual(10, sumOfConsInts(4))
		
	def testSumOfMultiples(self):
		self.assertEqual(8, sumOfMultiples(6,3,5))
		self.assertEqual(23, sumOfMultiples(10,3,5))
	
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
	#print answer
	print 'answer for n=1000:', sumOfMultiples(1000, 3, 5)