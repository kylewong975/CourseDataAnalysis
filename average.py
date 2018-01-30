import json, sys
from pprint import pprint

with open(sys.argv[1], 'r') as json_data:
	d = json.load(json_data)

# a dictionary with mapping from a subject (e.g., COM SCI) to the average 
# class size
subjectClassSizes = {}

# For each subject, there exists a list of class sizes. Loop through the 
# list and calculate the average of that list
for subject in d:
	classSizes = d[subject]
	total = 0
	numClasses = 0
	for classSize in classSizes:
		total += classSize
		numClasses += 1
	if numClasses != 0 and total != 0:
		subjectClassSizes[subject] = total / numClasses

# Convert python results back to json file
with open(sys.argv[2], 'w') as outfile:
	json.dump(subjectClassSizes, outfile)
	outfile.write("\n")