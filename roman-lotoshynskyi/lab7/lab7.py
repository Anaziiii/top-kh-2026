class Student:
    count = 0

    def __init__(self, name, course, score):
        self.name = name
        self.course = course
        self.score = score
        Student.count += 1

    def get_info(self):
        return f"Студент: {self.name} Курс: {self.course} Середній бал: {self.score}"

    @classmethod
    def get_count(cls):
        return f"Кількість студентів групи: {cls.count}"

    @classmethod
    def from_string(cls, student_data):
        name, course, score = student_data.split(",")
        return cls(name, int(course), int(score))

    @staticmethod
    def is_excellent(score):
        return score >= 60

student1 = Student("Лотошинський Роман", 2, 63)
student2 = Student("Іваць Максим", 2, 56)

student3 = Student.from_string("Кава Анастасія, 2, 87")

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

print(Student.get_count())

print("Чи студент здав предмет?")
print(student1.name, "-", Student.is_excellent(student1.score))
print(student2.name, "-", Student.is_excellent(student2.score))
print(student3.name, "-", Student.is_excellent(student3.score))