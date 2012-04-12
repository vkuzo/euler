"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import pow, sqrt
import unittest

def findPythTriplet(N):
	"""
	Returns a pythagorean triplet which sums to N
	If no such triplet exists, returns False
	"""
	
	# assume a^2 + b^2 = c^2
	# start with a = (N + 1) / 2, b = 1
	
	a = (N+1)/2
	while a > 0:
		for b in range(1, a+1):
			c = sqrt(pow(a,2) + pow(b,2))
			if a + b + c == N:
				return [a,b,int(c)]
		a -= 1
	return None
		
		#test this pythagorean triple

class testProblem(unittest.TestCase):	
	def setUp(self):
		pass
				
	def testGtstConsProduct(self):
		pass
		self.assertEqual([4,3,5], findPythTriplet(12))
		self.assertEqual([12,5,13], findPythTriplet(30))
	
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
	ans = findPythTriplet(1000)
	prod = ans[0] * ans[1] * ans[2]
	
	print 'the product abc where a^2 + b^2 = c^2 and a+b+c = 1000 is ', prod