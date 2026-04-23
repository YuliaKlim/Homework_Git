import randominfo
# person = randominfo.Person()
# print(person.full_name, person.gender, person.country, person.address)
try:
    person = randominfo.Person()
    print(person.full_name, person.gender, person.country, person.address)
except IndexError:
    print("Randominfo data base reading error. Please try again.")

