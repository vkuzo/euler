"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from p3 import getNextPrime
import unittest

def primes(n):
	"""
	Returns a list of the first n prime numbers
	"""
	primes = [2,3]
	for i in range(len(primes), n):
		primes.append(getNextPrime(primes))
	return primes[-1]

class testProblem(unittest.TestCase):	
	def setUp(self):
		pass
				
	def testGetNextPrime(self):
		self.assertEqual(19, getNextPrime([2,3,5,7,11,13,17]))
		self.assertEqual(23, getNextPrime([2,3,5,7,11,13,17,19]))
		
	def testPrimes(self):
		self.assertEqual(7, primes(4))
		self.assertEqual(13, primes(6))
				
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
	#print answer
	N = 10001
	print 'the 10001st prime number is', primes(N)