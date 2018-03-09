import json, sys
from pprint import pprint

json_objs = []

f = open(sys.argv[1], 'r')
for line in f:
	json_objs.append(json.loads(line))

# a dictionary with mapping from a subject (e.g., COM SCI) to the average 
# class size
output_contents = []
subjectClassSizesByClassType = {}
subjectClassSizesByLectureType = {}
subjectDiscussionSizes = {}

def func(line):
	subjectClassSizes = {}
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
	return subjectClassSizes

# For each subject, there exists a list of class sizes. Loop through the 
# list and calculate the average of that list

subjectClassSizesByClassType = func(json_objs[0])
subjectClassSizesByLectureType = func(json_objs[1])
output_contents.append(subjectClassSizesByClassType)
output_contents.append(subjectClassSizesByLectureType)

subjectDiscussionSizes = {}
for subject in json_objs[2]:
	discussionSizes = json_objs[2][subject]["discussionSizes"]
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

# Convert python results back to json file
with open(sys.argv[2], 'w') as outfile:
	for line in output_contents:
		json.dump(line, outfile)
		outfile.write("\n")

import operator
mean = lambda nums: sum(nums, 0.0) / len(nums)
average_lecture_size = round(mean([item["lecture"] for item in subjectClassSizesByLectureType.values() if "lecture" in item]), 2)
print ('Average Lecture Size: {}'.format(average_lecture_size))






