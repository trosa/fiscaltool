import string

def venue():
	venue = request.vars['id']
	people = []
	for letter in string.uppercase:
		people += get_people(letter, venue)
	return dict(people=people)

