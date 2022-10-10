#def build_person(first_name, last_name):
    #"""Return a dictionary of information about a person."""
    #person = {'first_name': first_name, 'last_name': last_name}
    #return person

#musician = build_person('jimi', 'hendrix')
#print(musician)

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    person['first_name'] = first_name.title()
    person['last_name'] = last_name.title()
    return person

programmer = build_person('mahmoud', 'hefny', age=27)
print(programmer)


