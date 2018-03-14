import csv
import json
import sys

with open('classdata.json', 'r') as json_data:
	final_data = json.load(json_data)

def addToJson(quarter):
	if (quarter=='Fall'):
		lec_data = open('./Fall2017-data-dk.csv', 'r')
	elif (quarter=='Winter'):
		lec_data = open('./Winter2018-data-dk.csv', 'r')
	else:
		lec_data = open('./Spring2018-data-dk.csv', 'r')
	lec_data = csv.reader(lec_data)

	for major in lec_data:
		major_name = major[0]
		if (major_name=='major' or major_name==''):
			continue
		avg_lecTime_day_lower = major[1]
		avg_num_lec_week_lower = major[2]
		avg_lecTime_week_lower = major[3]
		avg_lecTime_day_upper = major[4]
		avg_num_lec_week_upper = major[5]
		avg_lecTime_week_upper = major[6]
		if major_name in final_data:
			final_data[major_name][quarter]['Upper']['avg_lecture_length_day'] = avg_lecTime_day_upper
			final_data[major_name][quarter]['Upper']['avg_num_lectures_week'] = avg_num_lec_week_upper
			final_data[major_name][quarter]['Upper']['avg_lecture_length_week'] = avg_lecTime_week_upper
			final_data[major_name][quarter]['Lower']['avg_lecture_length_day'] = avg_lecTime_day_lower
			final_data[major_name][quarter]['Lower']['avg_num_lectures_week'] = avg_num_lec_week_lower
			final_data[major_name][quarter]['Lower']['avg_lecture_length_week'] = avg_lecTime_week_lower

for i in ['Fall', 'Winter', 'Spring']:
	addToJson(i)

with open('finalData.json', 'w') as outfile:
	json.dump(final_data, outfile)
