class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class MarkCalculator(Student):
    def __init__(self, name, id, mark1, mark2, mark3, mark4):
        super().__init__(name, id)
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.mark4 = mark4
        
    def calculate_total(self):
        total = self.mark1 + self.mark2 + self.mark3 + self.mark4
        return total
    
    def calculate_average(self):
        total = self.calculate_total()
        average = total / 4
        return average

name = input("Enter student name: ")
id = input("Enter student ID: ")
mark1 = float(input("Enter mark in English: "))
mark2 = float(input("Enter mark in Math: "))
mark3 = float(input("Enter mark in Physics: "))
mark4 = float(input("Enter mark in Chemistry: "))

student = MarkCalculator(name, id, mark1, mark2, mark3, mark4)
total_marks = student.calculate_total()
average_marks = student.calculate_average()

print("Student Name:", student.name)
print("Student ID:", student.id)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
