import json, sys

# 1st parameter, class lecture size for Fall
# 2nd - winter, 3rd spring
# 4th parameter, class lecture length for Fall
# 5th - winter, 6th spring
# plus further processing
# JSON of this format:
'''
[
    <major>: {
        School: “Engineering”,
        NorthOrSouth: “South”,
        Fall: {
            Upper: {
                avg_lecture_size:
                avg_lecture_length_day:
                avg_num_lectures_week:
                avg_lecture_length_week:
            },
            Lower: {...}
        },
        Winter: {...},
        Spring: {...}
    },
    ...
]
'''
# open files and get objects
with open(sys.argv[1], 'r') as json_data:
	size_fall = json.load(json_data)

with open(sys.argv[2], 'r') as json_data:
	size_winter = json.load(json_data)

with open(sys.argv[3], 'r') as json_data:
	size_spring = json.load(json_data)

res = {}
depts = {}
for d in (size_fall[0], size_winter[0], size_spring[0]):
	depts.update(d)

# initialize res list, containing elements that are maps from string (major) to map
for subject in depts:
	#subjects.append(subject)
	res[subject] = {
		"School": "",
		"NorthOrSouth": "",
		"Fall": {
			"Upper": {
				"avg_lecture_size": 0.0,
				"avg_lecture_length_day": 0.0,
				"avg_num_lectures_week": 0.0,
				"avg_lecture_length_week": 0.0
			},
			"Lower": {
				"avg_lecture_size": 0.0,
				"avg_lecture_length_day": 0.0,
				"avg_num_lectures_week": 0.0,
				"avg_lecture_length_week": 0.0
			}
		},
		"Winter": {
			"Upper": {
				"avg_lecture_size": 0.0,
				"avg_lecture_length_day": 0.0,
				"avg_num_lectures_week": 0.0,
				"avg_lecture_length_week": 0.0
			},
			"Lower": {
				"avg_lecture_size": 0.0,
				"avg_lecture_length_day": 0.0,
				"avg_num_lectures_week": 0.0,
				"avg_lecture_length_week": 0.0
			}
		},
		"Spring": {
			"Upper": {
				"avg_lecture_size": 0.0,
				"avg_lecture_length_day": 0.0,
				"avg_num_lectures_week": 0.0,
				"avg_lecture_length_week": 0.0
			},
			"Lower": {
				"avg_lecture_size": 0.0,
				"avg_lecture_length_day": 0.0,
				"avg_num_lectures_week": 0.0,
				"avg_lecture_length_week": 0.0
			}
		}
	}

# get fall data upper and lower division average class sizes
for subject in size_fall[0]:
	if "upper" in size_fall[0][subject]:
		#print(subject, size_fall[0][subject]["upper"])
		res[subject]["Fall"]["Upper"]["avg_lecture_size"] = size_fall[0][subject]["upper"]
	if "lower" in size_fall[0][subject]:
		#print(subject, size_fall[0][subject]["lower"])
		res[subject]["Fall"]["Lower"]["avg_lecture_size"] = size_fall[0][subject]["lower"]

# get winter data upper and lower division average class sizes
for subject in size_winter[0]:
	if "upper" in size_winter[0][subject]:
		#print(subject, size_fall[0][subject]["upper"])
		res[subject]["Winter"]["Upper"]["avg_lecture_size"] = size_winter[0][subject]["upper"]
	if "lower" in size_winter[0][subject]:
		#print(subject, size_fall[0][subject]["lower"])
		res[subject]["Winter"]["Lower"]["avg_lecture_size"] = size_winter[0][subject]["lower"]

# get spring data upper and lower division average class sizes
for subject in size_spring[0]:
	if "upper" in size_spring[0][subject]:
		#print(subject, size_fall[0][subject]["upper"])
		res[subject]["Spring"]["Upper"]["avg_lecture_size"] = size_spring[0][subject]["upper"]
	if "lower" in size_spring[0][subject]:
		#print(subject, size_fall[0][subject]["lower"])
		res[subject]["Spring"]["Lower"]["avg_lecture_size"] = size_spring[0][subject]["lower"]

#print(json.dumps(res, indent=3))
with open(sys.argv[4], 'w') as outfile:
	json.dump(res, outfile, indent=3)
