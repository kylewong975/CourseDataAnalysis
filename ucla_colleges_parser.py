# Major definitions
LETTERS_AND_SCIENCE = [
	"African American Studies", 
	"African and Middle Eastern Studies", 
	"American Indian Studies", 
	"American Literature and Culture", 
	"Ancient Near East and Egyptology", 
	"Anthropology", 
	"Arabic",
	"Art History",
	"Asian American Studies",
	"Asian Humanities",
	"Asian Languages and Linguistics",
	"Asian Religions",
	"Asian Studies",
	"Astrophysics",
	"Atmospheric and Oceanic Sciences",
	"Biochemistry",
	"Biology",
	"Biophysics",
	"Business Economics",
	"Central and East European Languages and Cultures",
	"Chemistry",
	"Chemistry\/Materials Science",
	"Chicana and Chicano Studies",
	"Chinese",
	"Classical Civilization",
	"Cognitive Science",
	"Communication",
	"Comparative Literature",
	"Computational and Systems Biology",
	"Earth and Environmental Science",
	"Ecology, Behavior, and Evolution",
	"Economics",
	"Engineering Geology",
	"English",
	"Environmental Science",
	"European Studies",
	"French",
	"French and Linguistics",
	"Gender Studies",
	"Geography",
	"Geography\/Environmental Studies",
	"Geology",
	"Geophysics",
	"German",
	"Global Studies",
	"Greek",
	"Greek and Latin",
	"History",
	"Human Biology and Society",
	"International Development Studies",
	"Iranian Studies",
	"Italian",
	"Italian and Special Fields",
	"Japanese",
	"Jewish Studies",
	"Korean",
	"Latin",
	"Latin American Studies",
	"Linguistics",
	"Linguistics and Anthropology",
	"Linguistics and Asian Languages and Cultures",
	"Linguistics and Computer Science",
	"Linguistics and English",
	"Linguistics and French",
	"Linguistics and Italian",
	"Linguistics and Philosophy",
	"Linguistics and Psychology",
	"Linguistics and Scandinavian Languages",
	"Linguistics and Spanish",
	"Linguistics, Applied",
	"Marine Biology",
	"Mathematics",
	"Mathematics, Applied",
	"Mathematics\/Applied Science",
	"Mathematics\/Atmospheric and Oceanic Sciences",
	"Mathematics\/Economics",
	"Mathematics, Financial Actuarial",
	"Mathematics for Teaching",
	"Mathematics of Computation",
	"Microbiology, Immunology, and Molecular Genetics",
	"Middle Eastern Studies",
	"Molecular, Cell, and Developmental Biology",
	"Neuroscience",
	"Nordic Studies",
	"Philosophy",
	"Physics",
	"Physiological Science",
	"Political Science",
	"Portuguese",
	"Psychobiology",
	"Psychology",
	"Religion, Study of",
	"Russian Language and Literature",
	"Russian Studies",
	"Scandinavian Languages and Cultures",
	"Sociology",
	"Spanish",
	"Spanish and Community and Culture",
	"Spanish and Linguistics",
	"Spanish and Portuguese",
	"Statistics"
]

ARTS_AND_ARCHITECTURE = [
	"Architectural Studies",
	"Art",
	"Dance",
	"Design | Media Arts",
	"World Arts and Cultures"
]

ENGINEERING_AND_APPLIED_SCIENCE = [
	"Aerospace Engineering",
	"Bioengineering",
	"Chemical Engineering",
	"Civil Engineering",
	"Computer Engineering",
	"Computer Science",
	"Computer Science and Engineering",
	"Electrical Engineering",
	"Materials Engineering",
	"Mechanical Engineering"
]

MUSIC = [
	"Ethnomusicology",
	"Music",
	"Music History"
]

NURSING = ["Nursing"]

THEATER_FILM_AND_TV = [
	"Film and Television",
	"Theater"
]

# functions that you can use to determine which class belongs to what college
# Number definitions
# 	1 = College of Letters and Science
# 	2 = School of the Arts and Architecture
# 	3 = School of Engineering and Applied Science
# 	4 = School of Music
# 	5 = School of Nursing
# 	6 = School of Theater, Film and Television
def whichCollege(course):
	if isTheaterFilmAndTV(course):
		return 6
	elif isNursing(course):
		return 5
	elif isMusic(course):
		return 4
	elif isEngineeringAndAppliedScience(course):
		return 3
	elif isArtsAndArchitecture(course):
		return 2
	elif isLettersAndScience(course):
		return 1
	else:
		for i in THEATER_FILM_AND_TV:
			if course.find(i) != -1:
				return 6
		for i in NURSING:
			if course.find(i) != -1:
				return 5
		for i in MUSIC:
			if course.find(i) != -1:
				return 4
		for i in ENGINEERING_AND_APPLIED_SCIENCE:
			if course.find(i) != -1:
				return 3
		for i in ARTS_AND_ARCHITECTURE:
			if course.find(i) != -1:
				return 2
		for i in LETTERS_AND_SCIENCE:
			if course.find(i) != -1:
				return 1
		return 0

def isLettersAndScience(course):
	paren = course.find("(") - 1
	item = course[0:paren]
	return item in LETTERS_AND_SCIENCE

def isArtsAndArchitecture(course):
	paren = course.find("(") - 1
	item = course[0:paren]
	return item in ARTS_AND_ARCHITECTURE

def isEngineeringAndAppliedScience(course):
	paren = course.find("(") - 1
	item = course[0:paren]
	return item in ENGINEERING_AND_APPLIED_SCIENCE

def isMusic(course):
	paren = course.find("(") - 1
	item = course[0:paren]
	return item in MUSIC

def isNursing(course):
	paren = course.find("(") - 1
	item = course[0:paren]
	return item in NURSING

def isTheaterFilmAndTV(course):
	paren = course.find("(") - 1
	item = course[0:paren]
	return item in THEATER_FILM_AND_TV
