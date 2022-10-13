class Student:

    number_of_students = 0

    def __init__(self, name, age, courses):
        self.name = name
        self.age = age 
        self.courses = courses

        Student.number_of_students += 1

    
    def descripe(self):
        print(f"Student name is: {self.name}")
        print(f"Student age is: {self.age}")
        print(f"Student courses are: {self.courses}")
        print("") 

    
    def is_old(self, number):
        if self.age <= number:
            print("Student isn't old")
        else:
            print("Student is old")

student1 = Student("Mahmoud", 20, ['CS', 'MATH'])
student2 = Student("Islam", 30, ['AI', 'NETWORKING'])
student3 = Student("Ibrahim", 40, ['DATA-STRUCTURES', 'WEB'])

student1.descripe()
student2.descripe()
student3.descripe()

student1.is_old(50)
