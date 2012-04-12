"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import unittest

def getNextPrime(primesList):
	"""
	Returns the next prime after primesList[-1], assuming all numbers in primesList are prime
	"""
	n = primesList[-1]
	keepGoing = True
	while keepGoing:
		n += 2 #assume that the last known prime number is odd (ignore 2)
		foundFactors = False
		for x in primesList:
			if n % x == 0:
				foundFactors = True
				break
		if not foundFactors:
			keepGoing = False
	return n
		
def factor(N):
	"""
	Returns a list of N factored into primes
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