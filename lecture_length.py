import json
import time
import csv
from pprint import pprint

base = {
    'major': {
        'school': 'Engineering',
        'NorthOrSouth': 'South',
        'Fall': {
            'upper': {
                'avg_lecture_size': 0,
                'avg_lecture_length_day': 0,
                'avg_num_lectures_week': 0,
                'avg_lecture_length_week': 0,
            },
            'lower': {
                'avg_lecture_size': 0,
                'avg_lecture_length_day': 0,
                'avg_num_lectures_week': 0,
                'avg_lecture_length_week': 0
            },
        },
        'Winter': {
            'upper': {
                'avg_lecture_size': 0,
                'avg_lecture_length_day': 0,
                'avg_num_lectures_week': 0,
                'avg_lecture_length_week': 0
            },
            'lower': {
                'avg_lecture_size': 0,
                'avg_lecture_length_day': 0,
                'avg_num_lectures_week': 0,
                'avg_lecture_length_week': 0
            },
        },
        'Spring': {
            'upper': {
                'avg_lecture_size': 0,
                'avg_lecture_length_day': 0,
                'avg_num_lectures_week': 0,
                'avg_lecture_length_week': 0
            },
            'lower': {
                'avg_lecture_size': 0,
                'avg_lecture_length_day': 0,
                'avg_num_lectures_week': 0,
                'avg_lecture_length_week': 0
            }
        }
    }
}

data = json.load(open('/Users/dinkar/Desktop/the_stack/CourseDataAnalysis/classData.json'))

majors = open('/Users/dinkar/Desktop/the_stack/CourseDataAnalysis/Fall2017-data-dk.csv', 'r')
majors = csv.reader(majors)
for l in majors:
    if (l[0]=='major' or l[0]==''):
        continue
    data[l[0]]


# output = {}
#
# def createJson():
#     for n,l in majors.items():
#         output[n] = base["major"]
#
#
# with open('data.json', 'w') as f:
#     createJson()
#     json.dump(output, f)
# print len(output)
