# CourseDataAnalysis
This repository features a parser (Python script) that reads the course list JSON file and produces a JSON output with 
relevant information used for data analysis. The course list JSON file contains a list of courses, each of which has
individual course information such as class size, lecture times, subject, course name, etc

### Instructions
- git clone this repository: `git clone https://github.com/kylewong975/CourseDataAnalysis.git`
- Go to the folder of the repository: `cd CourseDataAnalysis`
- Make sure you are allowed to run the shell script: `chmod +x analyze.sh`
- Run the shell script, passing in the input JSON file as the first argument and the output JSON file as the second argument. Make sure both of these files exist and input JSON file can be read and output JSON file can be written. Every iteration of the shell script will remove whatever contents you currently have in the output JSON file and writes the new output to that output JSON file. `./analyze.sh [inputFile] [outputFile]`
  - If you choose to run the python script directly, you can run it using: `python classDataParser.py` or `python3 classDataParser.py` passing your input JSON file and output JSON file as parameters. However, I recommend using the shell script since I formatted the input JSON file slightly differently, temporarily, to accomodate json.load() in python.

### Files
- `classDataParser.py`: This Python script parses the course list JSON file and produces a JSON output with relevant 
information used for data analysis.
- `analyze.sh`: A shell script that runs the Python script `classDataParser.py`
- `sampleCourses.json`: Because the official myUCLA courses JSON should be remain private, I made this sample JSON file 
detailing possible JSON objects that were found in myUCLA courses and possible edge cases to ensure my parser is robust.
