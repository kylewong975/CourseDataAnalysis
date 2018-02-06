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

# For each subject, there exists a list of class sizes. Loop through the 
# list and calculate the average of that list
for line in json_objs:
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

# Convert python results back to json file
with open(sys.argv[2], 'w') as outfile:
	for line in output_contents:
		json.dump(line, outfile)
		outfile.write("\n")