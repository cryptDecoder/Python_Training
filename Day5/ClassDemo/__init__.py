class Student:
    def __init__(self,name,roll,dept, sub):
        self.name = name
        self.roll = roll
        self.dept = dept
        self.sub = sub


    def show_student_data(self):
        print(self.name, self.roll,self.dept,self.sub)


s = Student("Pruthvi",1654,"Computer", ['robotics', 'hpc', 'security'])
s.show_student_data()
