class Students:
    discount_amt = 200

    def __init__(self, first_name, last_name, tution_fee):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = f"{first_name}.{last_name}@std.kyrenia.edu.tr"
        self.tution_fee = tution_fee
        self.courses = []  # list of enrolled Course objects

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def apply_discount(self):
        self.tution_fee = int(self.tution_fee) - self.discount_amt
        return self.tution_fee

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.full_name()} has been enrolled in {course.course_name}.")
        else:
            print(f"{self.full_name()} is already enrolled in {course.course_name}.")

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.full_name()} has dropped {course.course_name}.")
        else:
            print(f"{self.full_name()} is not enrolled in {course.course_name}.")

    def list_courses(self):
        if not self.courses:
            print(f"{self.full_name()} is not enrolled in any courses.")
        else:
            print(f"{self.full_name()} is enrolled in:")
            for course in self.courses:
                print(f" - {course.course_name}")

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}', {self.tution_fee})"
    
    def __str__(self):
        return f"{self.full_name()} - {self.email_address}"
    
    def __add__(self, other):
        return self.tution_fee + other.tution_fee


class Course:
    def __init__(self, course_name, course_code, credits):
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits

    def __repr__(self):
        return f"Course('{self.course_name}', '{self.course_code}', {self.credits})"

    def __str__(self):
        return f"{self.course_name} ({self.course_code}) - {self.credits} credits"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Added student: {student.full_name()}")
        else:
            print(f"{student.full_name()} is already registered.")

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"Added course: {course.course_name}")
        else:
            print(f"{course.course_name} is already offered.")

    def enroll_student_in_course(self, student, course):
        if student in self.students and course in self.courses:
            student.enroll(course)
        else:
            print("Error: Student or course not found in school records.")

    def list_students(self):
        print(f"\nStudents in {self.name}:")
        for s in self.students:
            print(f" - {s.full_name()} ({s.email_address})")

    def list_courses(self):
        print(f"\nCourses offered at {self.name}:")
        for c in self.courses:
            print(f" - {c.course_name} ({c.course_code})")

    def summary(self):
        print(f"\n🏫 School Summary for {self.name}")
        print(f"Total Students: {len(self.students)}")
        print(f"Total Courses: {len(self.courses)}")


# --- Example Usage ---

# Create school
kyrenia = School("Kyrenia University")

# Create students
rae = Students('Rae', 'Wale', 8000)
lee = Students('Lee', 'Min', 9000)

# Create courses
math101 = Course('Mathematics', 'MATH101', 3)
cs103 = Course('Computer Science', 'CS103', 4)

# Add to school
kyrenia.add_student(rae)
kyrenia.add_student(lee)
kyrenia.add_course(math101)
kyrenia.add_course(cs103)

# Enroll students in courses
kyrenia.enroll_student_in_course(rae, math101)
kyrenia.enroll_student_in_course(lee, cs103)
kyrenia.enroll_student_in_course(rae, cs103)

# List data
kyrenia.list_students()
kyrenia.list_courses()
kyrenia.summary()

# Show student's enrolled courses
rae.list_courses()
