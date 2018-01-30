import json
from pprint import pprint

with open('Fall2017.json', 'r') as json_data:
	d = json.load(json_data)

# a dictionary with mapping from a subject (e.g., COM SCI) to a list of class 
# sizes
subjectClassSizes = {}

for courses in d:
	subject = courses["fields"]["subject"]
	if subject in subjectClassSizes:
		subjectClassSizes[subject].append(100)
	else:
		subjectClassSizes[subject] = [100]

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
# for courses in d:
#	status = courses["fields"]["statuses"]


pprint(subjectClassSizes)

# Convert python results back to json file
'''
with open('Fall2017-Subject-ClassSize.json', 'w') as outfile:
	json.dump(d, outfile);
'''