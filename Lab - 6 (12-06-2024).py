import pickle

class CourseGrade:
    def __init__(self):
        self.course = ""
        self.stu_id = []
        self.grade = []

    def create_entry (self):
        self.course = input ("Student's course: ")
        n = int(input ("Enter the number of students: "))
        for x in range (0, n):
            a = int(input ("Student ID: "))
            b = int(input ("Grade: "))
            self.stu_id.append (a)
            self.grade.append (b)


c = CourseGrade()
c.create_entry()
d = CourseGrade()
d.create_entry()
e = CourseGrade()
e.create_entry()
g = CourseGrade()
g.create_entry()

f =open ('grades_info.dat', 'ab')

pickle.dump(c,f)
pickle.dump(d,f)
pickle.dump(e,f)
pickle.dump(g,f)
f.close()

f = open('grades_info.dat', 'rb')
while True:
    try:
        data = pickle.load(f)
        print("Course Name: ",data.course)
        print("Student ID: ", data.stu_id)
        print("Grades: ", data.grade)
    except EOFError:
        break
f.close()