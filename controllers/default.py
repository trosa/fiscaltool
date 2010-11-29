import string

def index():
    if 'id' not in request.vars:
        return dict(people='')
    venue = request.vars['id']
    people = []
    for letter in string.uppercase:
        people += get_people(letter, venue)
    return dict(people=people)
