mydict = {'A':3,'B':5,'C':0,'D':2}
total = {'A':3,'B':5,'C':2}
votes = {'A':112,'B':52,'C':2,'D':36}
seats =  {'A':3,'B':1,'C':0,'D':1}
myd1 = {'A':3,'B':1,'C':6,'D':1}
myd2 = {'X':5,'A':1,'Y':3,'D':7}
#Exercise 1

def getTotal(d): 
	sum = 0
	for value in d.values():
		sum += value
	return sum 


#Exercise 2

def normalise(d:int):
	sum = getTotal(d) 
	for key, value in d.items():
		value = value/sum
		d[key] = value
	return d

# print(normalise(total))

#Exercise 3

def printNonZero(d:int):
	for keys, values in d.copy().items():
		if values == 0:
			d.pop(keys)
			for key, value in d.items():
				print(key,':',value)
			return


#Exercise 4

def analyse(votes,seats):
	voteCount = normalise(votes)
	seatCount = normalise(seats)
	for keys, values in voteCount.copy().items():
		values = values * 100
		if values < 1:
			voteCount.pop(keys)
		else:
			print(keys,':',int(values),'%','of votes vs',int(seatCount[keys]*100),'%','of seats')
	return

#Exercise 5
def addTo(d1,d2):
	for key in d2:
		if key in d1:
			d1[key] += d2[key]
		else:
			d1[key] = d2[key]
	return d1

#Exercise 6
def getConstituencies(filename):
	constituencySet = set()
	file = open(filename, "r")
	constituencies = file.readlines()
	file.close()
	for i, line in enumerate(constituencies):
		if "_Constituency:" in line: 
			for constituency in constituencies[i:i+1]: 
				final = constituency.rstrip().split(':')[1]
				constituencySet.add(final)
	return constituencySet

#Exercise 7
def getParties(filename):
	partySet = set()
	file = open(filename, "r")
	parties = file.readlines()
	for i, line in enumerate(parties):
		for party in parties[i:i+1]:
			final = party.rstrip().split(':')[0]
			partySet.add(final)
			partySet.discard('_Constituency')
			partySet.discard('_Seats')
			partySet.discard('')
	file.close()
	return partySet

#Exercise 8

def getVotesForConstituency(filename,constituency:str):
	voteSet = {}
	file = open(filename)
	lineList = file.readlines()
	lineNo = 0
	while lineNo < len(lineList) and lineList[lineNo].strip() != "_Constituency:" + constituency:
		lineNo += 1
	lineNo += 1
	while lineNo < len(lineList) and lineList[lineNo].strip() != '':
		info = lineList[lineNo+1].strip()
		final = info.split(':')
		for value in final:
			if value != '':
				voteSet[final[0]] = final[1]
		lineNo += 1
	return voteSet

	myfile.close()

#Exercise 9

def getTotalVotes(filename):
	file = open(filename)
	total = 0
	parties = getParties(filename)
	votes = {}
	for party in parties:
		for line in file.readlines():
			info = line.strip().split(':')
			if info[0] != '_Seats' and info[0] != '_Constituency' and info[0] != '':
				if info[0] in votes:
					votes[info[0]] += int(info[1])
				else:
					votes[info[0]] = int(info[1])
	return votes

#Exercise 10
def getTotalSeats(filename):
  voteFile = open(filename)
  seats = None
  votes = {}
  totalSeats = {}
  numSeats = -1
  winner = (0,None)
  for line in voteFile:
    lineSplit = line.strip().split(':')
    if line.strip() == '' and seats != {}:
      while numSeats > 0 :
        winner = (-1,None)
        for party in votes:
          if winner[0] < (votes[party]/(1 + seats[party])):
            winner = (votes[party]/(1 + seats[party]), party)
        seats[winner[1]] += 1
        numSeats -= 1
      for party in seats:
        if party not in totalSeats and seats[party] > 0:
          totalSeats[party] = seats[party]
        elif seats[party] > 0 :
          totalSeats[party] += seats[party]
      seats = {}
    elif lineSplit[0] =='_Seats':
      numSeats = int(lineSplit[1])
    elif lineSplit[0] == '_Constituency':
      seats = {}
      votes = {}
    elif line.strip() != '':
      # Read all the seats
      votes[lineSplit[0]] = int(lineSplit[1])
      seats[lineSplit[0]] = 0
  return totalSeats
print(getTotalSeats('ukeu2019.txt'))

# Expected Output:
# >>> seats = getTotalSeats('ukeu2019.txt')
# >>> printNonZero(seats)
# Brexit Party : 29
# Liberal Democrats : 16
# Labour : 10
# Conservative : 4
# Green : 7
# SNP : 3
# Plaid Cymru : 1

# print(getVotesForConstituency('ukeu2019.txt','London'))

getTotalSeats('ukeu2019.txt')





