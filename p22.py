"""
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working 
out the alphabetical value for each name, multiply this 
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""

import re
import unittest

ALPHABET = dict([(x[1],x[0]) for x in enumerate('abcdefghijklmnopqrstuvwxyz'.upper(),start=1)])

def getNames(fileName):
	"""
	Returns a list of names in fileName
	"""
	f = open(fileName,'r')
	s = re.sub(r'["]','',f.read())
	return sorted(s.split(','))
	
def alphabetScore(s):
	"""
	Returns the alphabet score of s
	"""
	return sum([ALPHABET[x] for x in s])

class testProblem(unittest.TestCase):
	def setUp(self):
		pass
		
	def testALPHABET(self):
		self.assertEquals(24, ALPHABET['X'])
		
	def testGetNames(self):
		self.assertEquals('COLIN', getNames('p22_names.txt')[937])
		
	def testAlphabetScore(self):
		self.assertEquals(53, alphabetScore(getNames('p22_names.txt')[937]))
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)

	myList = enumerate([alphabetScore(s) for s in getNames('p22_names.txt')], start=1)
	mySum = sum([x[0]*x[1] for x in myList])
	print mySum
	