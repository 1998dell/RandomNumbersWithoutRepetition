import random as r

i = 1
numLen = 42
numDraw = 6
numList = []

def isDup(randNum, numList):
	isDup = False
	for x in numList:
		if randNum == x:
			isDup = True
			return isDup
			break
	return isDup

while i < numDraw+1 :
	randNum = r.randrange(1,numLen+1)
	if not isDup(randNum, numList):
		numList.append(randNum)
		i+=1

print(numList)
