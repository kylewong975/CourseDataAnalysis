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

# Determine if the class is lower division (1-99), upper division
# (100-199), graduate (200-299), teacher training (300-399), professional
# courses (400-499), or individual study and research (500-599)
# Edge cases: 
# 	If the course is multiple listed (M before number)
# 	Some courses are C### e.g., C127
#	Some courses are Writing II (W after number)
# 	Course series (e.g., Math 32A, 32B, 33A, ...)
def findClassType(course):
	end = course.find("-") - 1
	start = course.rfind(" ", 0, end - 1)
	val = course[start+1:end]
	courseNum = filter(lambda x: x.isdigit(), val)
	# lower division
	if courseNum >= 1 and courseNum <= 99:
		return "lower"
	# upper division
	elif courseNum >= 100 and courseNum <= 199:
		return "upper"
	# graduate courses
	elif courseNum >= 200 and courseNum <= 299:
		return "grad"
	# teacher training
	elif courseNum >= 300 and courseNum <= 399:
		return "teach"
	# professional courses
	elif courseNum >= 400 and courseNum <= 499:
		return "prof"
	# individual study and research
	elif courseNum >= 500 and courseNum <= 599:
		return "indiv"
	# invalid course number
	else:
		return "invalid"

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
	course = courses["pk"]
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