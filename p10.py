"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

def sumPrimesBelow(N):
	"""
	Returns the sum of primes below N
	"""
	s = 2 #first prime number is 2
	for i in range(3,N,2): #start with 3; step by 2 to avoid even numbers
		if isPrime(i):
			s+= i
	return s

class testProblem(unittest.TestCase):	
	def setUp(self):
		pass
		
	def testIsPrime(self):
		self.assertEquals(True, isPrime(17))
		self.assertEquals(True, isPrime(23))
		self.assertEquals(False, isPrime(15))		
		self.assertEquals(False, isPrime(25))		
				
	def testSumPrimesBelow(self):
		self.assertEquals(17, sumPrimesBelow(10))
		self.assertEquals(77, sumPrimesBelow(20))
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
	print 'the sum of all primes below two million is ', sumPrimesBelow(2*pow(10,6))