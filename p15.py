"""
Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 2020 grid?
"""

import unittest

def getMatrix(n):
	"""
	Returns an (n+1) by (n+1) matrix result of ways to get from result[i,j] to result[-1,-1]
	
	for n = 2, should return
	
	[[6,3,1],
	 [3,2,1],
	 [1,1,1]
	 ]
	"""
	res = []
	for i in range(n+1):
		res.append([0]*(n+1))
	
	#build the origin
	res[0][0] = 1
	
	#build the edges
	for x in range(1, len(res)):
		res[x][0] = res[x-1][0]
	
	for y in range(1, len(res)):
		res[0][y] = res[0][y-1]
	
	#build the inside
	for x in range(1,len(res)):
		for y in range(1, len(res)):
			res[x][y] = res[x-1][y] + res[x][y-1]
			
	return res

class testProblem(unittest.TestCase):
	def setUp(self):
		pass
		
	def testGetMatrix(self):
		pass
		self.assertEquals([[1,1,1],[1,2,3],[1,3,6]], getMatrix(2))
		
if __name__ == '__main__':
	#test
	suite = unittest.TestLoader().loadTestsFromTestCase(testProblem)
	unittest.TextTestRunner(verbosity=2).run(suite)

	print getMatrix(20)[-1][-1]