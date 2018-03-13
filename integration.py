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
with open(sys.argv[1], 'r') as json_data:
	size_fall = json.load(json_data)

res = {}
subjects = []

# initialize res list, containing elements that are maps from string (major) to map
for subject in size_fall[0]:
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


for subject in size_fall[0]:
	if "upper" in size_fall[0][subject]:
		#print(subject, size_fall[0][subject]["upper"])
		res[subject]["Fall"]["Upper"]["avg_lecture_size"] = size_fall[0][subject]["upper"]
	if "lower" in size_fall[0][subject]:
		#print(subject, size_fall[0][subject]["lower"])
		res[subject]["Fall"]["Lower"]["avg_lecture_size"] = size_fall[0][subject]["lower"]
print(json.dumps(res, indent=3))
