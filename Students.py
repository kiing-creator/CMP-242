class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):   
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"There is a total number of {cls.count} students"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"



Student1 = Student(name="Rae", gpa=3.2)
Student2 = Student(name="Wale", gpa=3.4)
Student3 = Student(name="Cell", gpa=3.6)
Student4 = Student(name="Zed", gpa=3.0)

print(Student1.get_info())
print(Student.get_count())
print(Student.get_average_gpa())
