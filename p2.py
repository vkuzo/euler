"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

from math import pow
import unittest

def fibSequence(N):
	"""
	Iteratively returns terms in the Fibbonaci sequence as long as they are less than N
	"""
	#initialize
	n1 = 0
	n2 = 1
	#return the first two values
	yield n1
	yield n2
	#return the rest of the values up to the upper bound - 1
	while n1 + n2 < N:
		n1, n2 = n2, n1 + n2
		yield n2

def sumEvenTerms(seq):
	"""
	Returns sum of all even terms in seq
	"""
	return sum([x for x in seq if x % 2 == 0])

class testProblem(unittest.TestCase):	
	def setUp(self):
		pass
		
	def testFibSequence(self):
		self.assertEqual([0,1,1,2,3,5,8], list(fibSequence(9)))

	def testSumEvenTerms(self):
		self.assertEqual(12, sumEvenTerms([1,2,3,4,5,6,7]))
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
	#print answer

	print 'sum below 4M:', sumEvenTerms(fibSequence(4 * pow(10,6)))