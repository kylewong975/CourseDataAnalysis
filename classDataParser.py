import json, sys
from pprint import pprint

with open(sys.argv[1], 'r') as json_data:
	d = json.load(json_data)

# a dictionary with mapping from a subject (e.g., COM SCI) to a list of class 
# sizes
subjectClassSizes = {}
# class sizes based on type (seminar, lecture, etc)
subjectClassSizes_type = {}
# a dictionary with mapping from a subject (e.g., COM SCI) to a list of 
# discussion sizes
'''
subject
	numDiscussions
	discussionSizes
'''
subjectDiscussionSizes = {}

# Extract course number from course name
def getCourseNumber(course):
	#edge case HIN-URD
	if course.find("HIN-URD") != -1:
		end = course.find("-", course.find("HIN-URD") + 6) - 1
	else:
		end = course.find("-") - 1
	start = course.rfind(" ", 0, end - 1)
	val = course[start+1:end]
	courseNum = ''.join(list(filter(lambda x: x.isdigit(), val)))
	if(len(courseNum) == 0):
		return -1
	return int(courseNum)

# Determine if the class is lower division (1-99), upper division
# (100-199), graduate (200-299), teacher training (300-399), professional
# courses (400-499), or individual study and research (500-599)
# Edge cases: 
# 	If the course is multiple listed (M before number)
# 	Some courses are C### e.g., C127
#	Some courses are Writing II (W after number)
# 	Course series (e.g., Math 32A, 32B, 33A, ...)
def findClassLevel(courseNum):
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

# Determine if the class is a regular lecture, laboratory, seminar, etc
def findClassType(section):
	# lecture
	if section.find("Lec") != -1:
		return "lecture"
	elif section.find("Lab") != -1:
		return "lab"
	elif section.find("Sem") != -1:
		return "seminar"
	elif section.find("Tut") != -1:
		return "tutorial"
	elif section.find("Rgp") != -1:
		return "research_group"
	else:
		return "unknown"

# Find the number of discussions and discussion sizes of the class in a 
# given subject
def findDiscussions(subject, section, status):
	if(findClassSize(status) <= 0):
		return
	# discussion section sizes can be trivially found by dividing lecture size
	# by number of discussions, but for robustness, return the list
	# discussion section statuses similar to classes, use findClassSize logic
	discussions = status.split("|*|")[1:] # the delimiter, omit lecture element
	for discussion in discussions:
		if(findClassSize(discussion) <= 0):
			continue
		subjectDiscussionSizes[subject]["numDiscussions"] += 1
		subjectDiscussionSizes[subject]["discussionSizes"].append(findClassSize(discussion))



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
	elif status.find("Closed by Dept") != -1:
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
	section = courses["fields"]["sections"]

	courseNum = getCourseNumber(course)
	classSize = findClassSize(status)
	classLevel = findClassLevel(courseNum)
	classType = findClassType(section)
	# Class size of < 0 means that it fails the string parsing of status,
	# indicating that it is either closed by dept or cancelled, so ignore 
	# such class status in our data analysis
	if classSize <= 0 or classLevel == "invalid":
		continue
	if subject not in subjectClassSizes:
		subjectClassSizes[subject] = {}
		for i in ["lower", "upper", "grad", "teach", "prof", "indiv"]:
			subjectClassSizes[subject][i] = []
		
	if subject not in subjectClassSizes_type:
		subjectClassSizes_type[subject] = {}
		for i in ["lecture", "lab", "seminar", "tutorial", "research_group", "unknown"]:
			subjectClassSizes_type[subject][i] = []

	if subject not in subjectDiscussionSizes:
		subjectDiscussionSizes[subject] = {}
		subjectDiscussionSizes[subject]["numDiscussions"] = 0
		subjectDiscussionSizes[subject]["discussionSizes"] = []

	subjectClassSizes[subject][classLevel].append(classSize)
	subjectClassSizes_type[subject][classType].append(classSize)
	if classType == "lecture":
		findDiscussions(subject, section, status)

# Convert python results back to json file
with open(sys.argv[2], 'w') as outfile:
	json.dump(subjectClassSizes, outfile)
	outfile.write("\n")
	json.dump(subjectClassSizes_type, outfile)
	outfile.write("\n")
	json.dump(subjectDiscussionSizes, outfile)
	outfile.write("\n")
