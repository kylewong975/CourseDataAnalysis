import json, sys
from pprint import pprint

json_objs = []

f = open(sys.argv[1], 'r')
for line in f:
	json_objs.append(json.loads(line))

# a dictionary with mapping from a subject (e.g., COM SCI) to the average 
# class size
output_contents = []
subjectClassSizes = {}
subjectDiscussionSizes = {}

lineNum = 1

# For each subject, there exists a list of class sizes. Loop through the 
# list and calculate the average of that list
for line in json_objs:
	if lineNum > 2:
		break
	for subject in line:
		for attr in line[subject]:
			classSizes = line[subject][attr]
			total = 0
			numClasses = 0
			for classSize in classSizes:
				total += classSize
				numClasses += 1
			if numClasses != 0 and total != 0:
				if subject not in subjectClassSizes:
					subjectClassSizes[subject] = {}
				subjectClassSizes[subject][attr] = total * 1.0 / numClasses
	output_contents.append(subjectClassSizes)
	subjectClassSizes = {}
	lineNum += 1
# For discussion section, similar logic but different JSON structure
lineNum = 1
for line in json_objs:
	if lineNum <= 2:
		lineNum += 1
		continue
	elif lineNum > 3:
		break
	for subject in line:
		discussionSizes = line[subject]["discussionSizes"]
		total = 0
		numDiscussions = 0
		for discussionSize in discussionSizes:
			total += discussionSize
			numDiscussions += 1
		if numDiscussions != 0 and total != 0:
			if subject not in subjectDiscussionSizes:
				subjectDiscussionSizes[subject] = {}
			subjectDiscussionSizes[subject]["discussionSize"] = total * 1.0 / numDiscussions
	output_contents.append(subjectDiscussionSizes)
	subjectDiscussionSizes = {}
	lineNum += 1

# Convert python results back to json file
with open(sys.argv[2], 'w') as outfile:
	for line in output_contents:
		json.dump(line, outfile)
		outfile.write("\n")