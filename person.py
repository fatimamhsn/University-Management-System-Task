class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
    

class Student(Person):
    def __init__(self, name, age, gender, studentID, course, grade):
        super().__init__(name, age, gender)
        self.studentID = studentID
        self.course = course
        self.grade = grade
        self.grades = []
        self.averagegrade = 0

    def set_students_details(self, student_ID, course):
        self.studentID = student_ID
        self.course = course

    def add_grade(self, grade):
        self.grades.append(grade)

    def calaculate_average_grade(self):
        value = 0
        for i in self.grades:
            value += i
        
        value = value/len(self.grades)
        self.averagegrade = value
        return value   

    def getstudentsummary(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender{self.gender}, ID: {self.studentID}, Course {self.course}, Average Grade: {self.averagegrade}")

    
class Professor(Person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(age, name, gender)
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def set_professor_details(self, staff_ID, department, salary):
        self.staff_ID  = staff_ID
        self.department = department
        self.salary = salary

    def give_feedback(Student,feedback):
        print(f'Feedback for{student.name}')

    


        
        

