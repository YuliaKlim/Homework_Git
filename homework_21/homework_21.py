from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "postgresql://postgres:postgres@localhost/academy"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    course_id = Column(Integer, ForeignKey('courses.id'))

    courses = relationship("Courses", back_populates="students")

class Courses(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name_course = Column(String)

    students = relationship("Students", back_populates="courses")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Adding courses
courses_list = [
    Courses(name_course = 'English B1'),
    Courses(name_course = 'English B2'),
    Courses(name_course = 'Python'),
    Courses(name_course = 'Java'),
    Courses(name_course = 'Manual Testing')
]
session.add_all(courses_list)
session.commit()

# Adding students
st1 = Students(name = 'Taras', age = 18, course_id = courses_list[0].id)
st2 = Students(name = 'Anna', age = 19, course_id = courses_list[1].id)
st3 = Students(name = 'Oleg', age = 20, course_id = courses_list[1].id)
st4 = Students(name = 'Dana', age = 22, course_id = courses_list[0].id)
st5 = Students(name = 'Dmytro', age = 24, course_id = courses_list[3].id)
st6 = Students(name = 'Yuliya', age = 25, course_id = courses_list[4].id)
st7 = Students(name = 'Olga', age = 30, course_id = courses_list[4].id)
st8 = Students(name = 'Nazar', age = 25, course_id = courses_list[2].id)
st9 = Students(name = 'Mark', age = 32, course_id = courses_list[2].id)
st10 = Students(name = 'Mariya', age = 23, course_id = courses_list[3].id)
st11 = Students(name = 'Sofiya', age = 21, course_id = courses_list[0].id)
st12 = Students(name = 'Oksana', age = 28, course_id = courses_list[1].id)
st13 = Students(name = 'Sergey', age = 27, course_id = courses_list[2].id)
st14 = Students(name = 'Nina', age = 31, course_id = courses_list[4].id)
st15 = Students(name = 'Zahar', age = 30, course_id = courses_list[1].id)
st16 = Students(name = 'Milaniya', age = 26, course_id = courses_list[2].id)
st17 = Students(name = 'Mikhail', age = 36, course_id = courses_list[2].id)
st18 = Students(name = 'Olesya', age = 29, course_id = courses_list[1].id)
st19 = Students(name = 'Oleksiy', age = 30, course_id = courses_list[3].id)
st20 = Students(name = 'Volodimir', age = 40, course_id = courses_list[2].id)

session.add_all([st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11, st12, st13, st14, st15, st16, st17, st18, st19, st20])
session.commit()

# Sample of students for the Python course
print(f'\n Students on Python')
course_python = session.query(Courses).filter_by(name_course = 'Python').first()
for student in course_python.students:
    print(f'Name: {student.name}')
    print(f'Age: {student.age}')

# Student age update
dmytro_db = session.query(Students).filter_by(name = 'Dmytro').first()
if dmytro_db:
    dmytro_db.age = 42
    session.commit()
    print(f'\n Updated {dmytro_db.name} age to {dmytro_db.age}')

# Deleting a student
taras_db = session.query(Students).filter_by(name = 'Taras').first()
if taras_db:
    session.delete(taras_db)
    session.commit()
    print(f'\n Student Taras deleted')

print(f'\n Current Students List')
for student in session.query(Students).all():
    print(f'Student: {student.name}, age: {student.age}, course_id: {student.course_id}')

session.close()