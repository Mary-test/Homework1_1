class Student:
    def __init__(self, name, surname, age, gender, institution, faculty, course, admissionnumber, marks):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.institution = institution
        self.faculty = faculty
        self.course = course
        self.admissionnumber = admissionnumber
        self.marks = marks
        def select_subscribtion(arg):
    print(arg.name, "has selected new subscription")
    def select_professor(arg):
        print(arg.name, "has selected Pr.Jones")
        def pass_exam(arg):
            print(arg.name, "has passed exams")
            student1 = Student("Mary", "Smith", 17, "female", "University1", "Mathematics", "first", 846488, 100)print(student1.name)
print(student1.admissionnumber)
student1.select_subscribtion()