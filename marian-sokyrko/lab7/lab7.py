class Student:
    student_count = 0

    def __init__(self, first_name, last_name, course, average_score):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.average_score = average_score
        self.full_name = f"{first_name} {last_name}"
        Student.student_count += 1

    def get_description(self):
        return f"Студент {self.full_name}, курс {self.course}, середній бал {self.average_score}"

    @classmethod
    def get_total_students(cls):
        return f"Загальна кількість студентів: {cls.student_count}"

    @classmethod
    def from_string(cls, student_str):
        first_name, last_name, course, average_score = student_str.split(",")
        return cls(first_name, last_name, int(course), float(average_score))

    @staticmethod
    def is_passing_grade(grade):
        return grade >= 60

student1 = Student("Мар'ян", "Сокирко", 2, 75)
student2 = Student("Орест", "Баган", 2, 90)

student3_data = "Максим, Іваць, 2, 85"
student3 = Student.from_string(student3_data)

print(student1.get_description())
print(student2.get_description())
print(student3.get_description())
print(Student.get_total_students())

test_score = 59
print(f"Чи є бал {test_score} прохідним? {Student.is_passing_grade(test_score)}")
print(f"Чи є бал {student1.average_score} прохідним? {Student.is_passing_grade(student1.average_score)}")
print(f"Чи є бал {student2.average_score} прохідним? {Student.is_passing_grade(student2.average_score)}")
print(f"Чи є бал {student3.average_score} прохідним? {Student.is_passing_grade(student3.average_score)}")