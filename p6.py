"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and 
the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from math import pow
import unittest

def diffSumSqSqSum(N):
	"""
	Returns the difference between the sum of the squares of the first N natural numbers and the square of the sum.
	"""
	sq_sum = pow(N*(N+1)/2, 2)
	sum_sq = (2*N + 1)*(N + 1)*N / 6
	return int(sq_sum - sum_sq)
	
	# alternate implementation - brute force
	# s = 0
	# for i in range(1, N+1):
		# for j in range(1, N+1):
			# if i <> j:
				# s += i*j
	# return s

class testProblem(unittest.TestCase):	
	def setUp(self):
		pass
		
	def testDiff(self):
		self.assertEqual(2640,diffSumSqSqSum(10))
		pass
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
	print 'the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is ', diffSumSqSqSum(100)