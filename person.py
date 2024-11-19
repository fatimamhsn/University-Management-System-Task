class Person:
    def __init__(self, given_name, given_age, given_gender):
        self.name = given_name
        self.age = given_age
        self.gender = given_gender

    def set_details(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        print(f"Name{self.name}, Age {self.age}, Gender: {self.gender}")
    

class Student(Person):
    def __init__(self, given_name, given_age, given_gender, studentID, given_course, given_grades):
        super().__init__(self, given_name, given_age, given_gender)
        self.studentID = studentID
        self.course = given_course
        self.grades = given_grades

    def set_students_details(self, student_ID, course):
        self.studentID = student_ID
        self.course = course

    def add_grade(self, grade):

    def getstudentsummary(self):
        print(f"Name: {name}, Age: {} ")


        
        

