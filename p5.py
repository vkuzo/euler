"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from collections import Counter
from math import pow
from p3 import getNextPrime #returns the next prime given a list of primes
import unittest

def getPrimes(uBound):
	"""
	Returns a list of primes smaller than or equal to uBound
	"""
	primes = [2,3]
	while primes[-1] <= uBound:
		primes.append(getNextPrime(primes))
	if primes[-1] > uBound:
		primes.pop()
	return primes

def factor(n):
	"""
	Returns a counter object with the factorization of x.  Multiple factors are repeated
	"""
	primes = getPrimes(n)
	keepGoing = True
	factors = Counter()
	nVar = n 
	for x in primes:
		keepGoing = True
		if nVar < x:
			break
		while nVar % x == 0:
			factors[x] += 1
			nVar = nVar / x
	return factors
	
def LCM(N):
	"""
	Returns the lowest common multiple of nubmers 2 through N, inclusive
	"""
	factors = Counter()
	for i in range(2,N+1):
		localFactors = factor(i)
		for x in localFactors:
			if factors[x] < localFactors[x]:
				factors[x] = localFactors[x]
	lcm = 1
	for x in factors:
		lcm = lcm * pow(x, factors[x])
	return int(lcm)
			
class testProblem(unittest.TestCase):	
	def setUp(self):
		pass
		
	def testGetNextPrime(self):
		self.assertEqual(19, getNextPrime([2,3,5,7,11,13,17]))
		self.assertEqual(23, getNextPrime([2,3,5,7,11,13,17,19]))

	def testGetPrimes(self):
		self.assertEqual([2,3,5], getPrimes(5))
		self.assertEqual([2,3,5,7,11,13,17,19], getPrimes(20))
		
	def testFactor(self):
		self.assertEqual(Counter({2:2, 3:1, 5:1}), factor(60))
		
	def testLCM(self):
		self.assertEqual(60, LCM(5))
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
	print 'the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is ', LCM(20)