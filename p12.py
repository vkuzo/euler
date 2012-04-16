"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10	
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

from collections import Counter
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

def factor(n, primes):
	"""
	Returns a counter object with the prime factorization of x.  Multiple factors are repeated
	"""
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

def triangleNumber(n):
	"""
	Returns the nth triangle number
	"""
	return n * (n + 1) / 2
		
def getNumDivisors(N, primes):
	"""
	Returns the # divisors of N
	"""
	numDivisors = 1
	
	#add all prime factors
	factors = factor(N, primes)
	
	for x in factors:
		numDivisors *= (factors[x] + 1)
	
	return numDivisors
	
def firstTriangleNumberNDivisors(N, primes):
	"""
	Returns the first triangle number with more than N divisors
	"""
	
	#start with the third triangle number
	n = 3
	keepGoing = True
	while keepGoing:
		tNum = triangleNumber(n)
		divLength = getNumDivisors(tNum, primes)
		print n, tNum, divLength
		if divLength > N:
			keepGoing = False
		else:
			n += 1
	return tNum
	
class testProblem(unittest.TestCase):
	def setUp(self):
		pass
		
	def testTriangleNumber(self):
		self.assertEquals(21, triangleNumber(6))
		self.assertEquals(28, triangleNumber(7))
		
	def testGetNumDivisors(self):
		self.assertEquals(4, getNumDivisors(6), getPrimes(10))
		self.assertEquals(6, getNumDivisors(28), getPrimes(30))
		
	def testFirstTriangleNumberNDivisors(self):
		
		self.assertEquals(28, firstTriangleNumberNDivisors(5))

if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)

	primes = getPrimes(1000000)	
	#print len(getDivisors(triangleNumber(5000)))
	print 'the value of the first triangle number to have over five hundred divisors is', firstTriangleNumberNDivisors(500, primes)