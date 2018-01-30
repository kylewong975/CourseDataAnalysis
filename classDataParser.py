'''
TODOs:
Classes that are seminars, tutorials, labs should consider ALL sections
Separate upper division vs lower division analysis
'''

import json, sys
from pprint import pprint

with open(sys.argv[1], 'r') as json_data:
	d = json.load(json_data)

# a dictionary with mapping from a subject (e.g., COM SCI) to a list of class 
# sizes
subjectClassSizes = {}

# To find class size, extract the last occurrence of number right before |*|
# This is because:
# 	A lecture will be the total number of spots for a given class
# 	Discussion section size is just an addend to the sum which yields the 
#	total number of spots for a given class
# case 1: class is still open ("Open: 25 of 25 Left")
# case 2: class is full (closed) ("Closed Class Full (20)"
# case 3: class is on waitlist (since this only shows waitlist spots
# available, "Waitlist: 0 of 5 Taken", ignore waitlist status

# Edge Cases: 
# 	Lecture only, no discussion, so no |*| delimiter
# 	Classes that are "Closed by Dept"
# 	Classes that are "Cancelled"
def findClassSize(status):
	classSize = 0
	# Class is open
	if status.find("Open") != -1:
		delim = status.find("Left")
		numIndex = status.rfind(" ", 0, delim - 2)
		classSize = int(status[numIndex+1:delim-1])
	elif status.find("Closed by Dept"):
		return -1
	# Class is full (closed)
	elif status.find("Closed Class Full") != -1:
		delimL = status.find("(")
		delimR = status.find(")")
		classSize = int(status[delimL+1:delimR])
	return classSize

# Putting it all together
for courses in d:
	subject = courses["fields"]["subject"]
	status = courses["fields"]["statuses"]
	classSize = findClassSize(status)
	# Class size of < 0 means that it fails the string parsing of status,
	# indicating that it is either closed by dept or cancelled, so ignore 
	# such class status in our data analysis
	if classSize <= 0:
		continue
	if subject in subjectClassSizes:
		subjectClassSizes[subject].append(classSize)
	else:
		subjectClassSizes[subject] = [classSize]

# pprint(subjectClassSizes)

# Convert python results back to json file
with open(sys.argv[2], 'w') as outfile:
	json.dump(subjectClassSizes, outfile)
	outfile.write("\n")