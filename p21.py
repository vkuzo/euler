"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
 If d(a) = b and d(b) = a, where a  b, then a and b are an 
 amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math
from p12 import factor, getPrimes
import unittest

PRIMES = getPrimes(10001)

def sumProperDivisors(n, PRIMES):
	"""
	Returns the sum of the proper divisors of n
	"""
	factors = factor(n, PRIMES)
	s = 1
	for x in factors:
		s *= (math.pow(x, factors[x]+1)-1) / (x - 1)
	return int(s) - n

class testProblem(unittest.TestCase):
	def setUp(self):
		pass
		
	def testSumProperDivisors(self):
		self.assertEquals(16, sumProperDivisors(12, PRIMES))
		self.assertEquals(42, sumProperDivisors(30, PRIMES))
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)
		
	candidates = range(1,10000)
	amicable = []
	rejected = []
	for x in candidates:
		if (x not in amicable) and (x not in rejected):
			sumDivisors = sumProperDivisors(x, PRIMES)
			sumOtherDivisors = sumProperDivisors(sumDivisors, PRIMES)
			if x == sumOtherDivisors and x != sumDivisors:
				amicable.append(x)
				amicable.append(sumDivisors)
			else:
				rejected.append(x)
				rejected.append(sumDivisors)
	
	print sum(amicable)