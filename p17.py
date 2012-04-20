"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

import re
import unittest

ONES = {
	0:'zero',
	1:'one',
	2:'two',
	3:'three',
	4:'four',
	5:'five',
	6:'six',
	7:'seven',
	8:'eight',
	9:'nine'
	}
	
TEN_TO_NINETEEN = {
	10:'ten',
	11:'eleven',
	12:'twelve',
	13:'thirteen',
	14:'fourteen',
	15:'fifteen',
	16:'sixteen',
	17:'seventeen',
	18:'eighteen',
	19:'nineteen',
}

TENS = {
	10:'ten',
	20:'twenty',
	30:'thirty',
	40:'forty',
	50:'fifty',
	60:'sixty',
	70:'seventy',
	80:'eighty',
	90:'ninety'
}

def intToWord(n):
	"""
	Returns the English representation of n
	assumes 1 < n <= 1000
	"""
	
	s = ''
	
	if n == 1000: 
		s = 'one thousand'
	else:
		
		# find out hundreds
		hundreds = int(float(n) / 100.0)
		tens = int(float(n - hundreds*100) / 10.0)
		ones = int(n - hundreds*100 - tens*10)
		
		if 0 < hundreds:
			s += ONES[hundreds]
			s += ' hundred '
			if tens > 0 or ones > 0:
				s += 'and '
		
		if 1 == tens:
			s += TEN_TO_NINETEEN[tens*10 + ones]
		elif 1 < tens:
			s += TENS[tens*10]
			s += ' '
		
		if 0 < ones and 1 <> tens:
			s += ONES[ones]
	
	return s.strip()
	
def numOfLetters(s):
	"""
	Returns the number of alphanumeric chars in s
	"""
	return len(re.sub(r'[\W]','',s))

class testProblem(unittest.TestCase):
	def setUp(self):
		pass
		
	def testIntToWord(self):
		pass
		self.assertEquals('one thousand', intToWord(1000))
		self.assertEquals('two hundred and seventeen', intToWord(217))
		self.assertEquals('two hundred and twenty five', intToWord(225))
		self.assertEquals('seventy four', intToWord(74))
		self.assertEquals('seven hundred and two', intToWord(702))
		self.assertEquals('fifteen', intToWord(15))
		self.assertEquals('two', intToWord(2))
		
	def testNumOfLetters(self):
		pass
		self.assertEquals(8, numOfLetters('234 afs - 12'))
		self.assertEquals(23, numOfLetters(intToWord(342)))
		self.assertEquals(20, numOfLetters(intToWord(115)))
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)

	s = ''
	for i in range(1,1000+1):
		s += intToWord(i)
	print numOfLetters(s)