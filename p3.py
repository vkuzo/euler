"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
import unittest

def isPrime(n):
	"""
	Returns True if n is prime, False otherwise
	"""
	if n <= 1: return False
	elif n < 4: return True #2, 3
	elif n % 2 == 0: return False
	elif n < 9: return True #5, 7
	elif n % 3 == 0: return False
	else:
		#make use of the fact that all primes > 5 have have the form 6k +- 1
		r = math.floor(math.sqrt(n))
		f = 5
		while f <= r:
			if n % f == 0: return False
			if n % (f + 2) == 0: return False
			f += 6
		return True

def getNextPrime(primesList):
	"""
	Returns the next prime after primesList[-1], assuming all numbers in primesList are prime
	"""
	n = primesList[-1]
	keepGoing = True
	while keepGoing:
		n += 2 #assume that the last known prime number is odd (ignore 2)
		if isPrime(n):
			return n

def factor(N):
	"""
	Returns a list of N factored into primes
	Multiple prime factors are omitted
	"""
	#initialize
	primes = [2,3]
	factors = []
	n = N
	#test each known prime
	keepGoing = True
	while keepGoing:
		for x in primes: #skip 1
			if n % x == 0:
				factors.append(x)
				n = n / x
				break
		if n > primes[-1]:
			primes.append(getNextPrime(primes))
		elif n == 1:
			keepGoing = False
	return factors
		
class testProblem(unittest.TestCase):	
	def setUp(self):
		pass
				
	def testIsPrime(self):
		self.assertEquals(True, isPrime(17))
		self.assertEquals(True, isPrime(23))
		self.assertEquals(False, isPrime(15))		
		self.assertEquals(False, isPrime(25))		
				
	def testGetNextPrime(self):
		self.assertEqual(19, getNextPrime([2,3,5,7,11,13,17]))
		self.assertEqual(23, getNextPrime([2,3,5,7,11,13,17,19]))
		
	def testFactor(self):
		self.assertEqual([2,3], factor(6))
		self.assertEqual([2,3,7], factor(42))
		self.assertEqual([11,13], factor(143))
		self.assertEqual([2,2,2,3], factor(24))
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
	#print answer
	N = 600851475143
	print 'largest prime factor of %s is %s' % (N, factor(N)[-1])