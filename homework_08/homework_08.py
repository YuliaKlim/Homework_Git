class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def set_average_score(self, value):
        if type(value) is int:
            self.average_score = value

student_first = Student('Yuliia', 'Klimenko', 45, 100)

print(f'Name: {student_first.name}')
print(f'Surname: {student_first.surname}')
print(f'Age: {student_first.age}')
print(f'Average score: {student_first.average_score}')

student_first.set_average_score(90)
print(f'Average score after update: {student_first.average_score}')