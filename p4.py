"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from math import pow
import unittest

def isPalindrome(s):
	"""
	Returns True if s is a palindrome
	"""
	return str(s) == str(s)[::-1]
	
def largestPalindrome(d):
	"""
	Returns largest palindrome as a product of two d-digit numbers
	"""
	
	maxPalindrome = 0
	
	# iterate through possible products of three digit numbers
	lBound = int(pow(10,d-1))
	uBound = int(pow(10,d) - 1)
	for i in reversed(xrange(lBound, uBound + 1)):
		for j in reversed(xrange(i, uBound + 1)):
			prod = i*j
			
			# test if numbers are too small and we should break out
			if prod <= maxPalindrome:
				break
			
			# test for palindromes
			if isPalindrome(prod):
				if maxPalindrome < prod:
					maxPalindrome = prod
	
	return maxPalindrome
	

class testProblem(unittest.TestCase):	
	def setUp(self):
		pass
				
	def testIsPalindrome(self):
		self.assertEqual(True, isPalindrome(12345654321))
		self.assertEqual(True, isPalindrome(1234554321))
		self.assertEqual(False, isPalindrome(0123454321))
	
	def testLargestPalindrome(self):
		self.assertEqual(9009, largestPalindrome(2))
		
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
	print 'largest palindrome from the product of two 3 digit numbers is ', largestPalindrome(3)