class Student:

    student_count = 0
    def __init__(self, name, midterm_score, exam_score):
        self.name = name
        self.midterm = midterm_score
        self.exam = exam_score
        self.average_score = (self.midterm + self.exam) / 2

        Student.student_count += 1

    def get_report(self):
        return f"Студент: {self.name} | Середній бал: {self.average_score}"

    @classmethod
    def get_total_students(cls):
        return f"Загальна кількість студентів: {cls.student_count}"


student1 = Student("Олександр", 80, 90)
student2 = Student("Марія", 95, 100)

print(student1.get_report())
print(student2.get_report())