"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and 
it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import time
from p12 import getPrimes
from p21 import sumProperDivisors
import unittest

PRIMES = getPrimes(28124)

def isAbundant(n):
	"""
	Returns true if n is abundant
	"""
	return sumProperDivisors(n, PRIMES) > n

class testProblem(unittest.TestCase):
	def setUp(self):
		pass
		
	def testSumProperDivisors(self):
		self.assertEquals(28, sumProperDivisors(28, PRIMES))
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)

	#find all abundant numbers less than 28123
	start = time.clock()
	abundants = [i for i in range(1,28123) if isAbundant(i)]
	print abundants[:10]
	print time.clock() - start
	#for i in range(28123):
	#	if isAbundant(i):
	#		abundants.append(i)
	
	#find all numbers which can be expressed as the sum of two abundant numbers
	#sums = [abundants[i] + abundants[j] for i in range(len(abundants)) for j in range(i, len(abundants)) 
	#	if abundants[i] + abundants[j] <= 28123]
	sums = set()
	for i in range(len(abundants)):
		for j in range(i, len(abundants)):
			s = abundants[i] + abundants[j]
			if s <= 28123:
				sums.add(s)
			else:
				break
	print time.clock() - start
			
	#start with all numbers less than or equal to 28123 and remove known sums
	all_nums = set(range(28123))
	results = sorted(list(all_nums - sums))
	#results = [i for i in range(28123) if not (i in sums)]
	
	print sum(results)
	print results[:25]
	print results[-25:]