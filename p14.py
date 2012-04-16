"""
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13  40  20  10  5  16  8  4  2  1

or

5 16 8 4 2 1
7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import math
import unittest

def calculateSeqLength(startNum, knownLengths=[]):
	"""
	Returns the sequence length based on the sequence above
	"""
	n = startNum
	seqLength = 0
	while n > 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3*n + 1
		if n in knownLengths:
			return seqLength + knownLengths[n] 
		seqLength += 1
	# add one more for n = 1
	seqLength += 1 
	return seqLength

class testProblem(unittest.TestCase):
	def setUp(self):
		pass
		
	def testCalculateSeqLength(self):
		pass
		self.assertEquals(10, calculateSeqLength(13))
		self.assertEquals(6, calculateSeqLength(5))
		self.assertEquals(17, calculateSeqLength(7))
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)

	n = int(math.pow(10,6))
	results = {}
	
	#build sequence of results
	for i in range(2,n):
		res = calculateSeqLength(i, results)
		#print i, res
		results[i] = res
	
	#calculate the maximum result
	print max(results.iteritems(), key = lambda x: x[1])
	