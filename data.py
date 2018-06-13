#example data
from random import *
import names



def PopulateData():
	f = open('aadharids.txt', 'w')
	for i in range(0, 100):
		aadhar = randrange(100000000000, 999999999999,1)
		f.write(str(aadhar)+"\n")




PopulateData()