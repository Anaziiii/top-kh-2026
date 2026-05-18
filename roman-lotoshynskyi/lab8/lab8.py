class Student:
    count = 0

    def __init__(self, name, course, score):
        self.name = name
        self.course = course
        self.score = score
        Student.count += 1

    def get_info(self):
        return f"Студент: {self.name}, Курс: {self.course}, Середній бал: {self.score}"

    @classmethod
    def get_count(cls):
        return f"Кількість студентів: {cls.count}"


class Monitor(Student):
    def __init__(self, name, course, score, group):
        super().__init__(name, course, score)
        self.group = group

    def get_monitor_info(self):
        return f"{self.name} є старостою групи {self.group}"

class Teacher(Student):
    def __init__(self, name, course, score, subject):
        super().__init__(name, course, score)
        self.subject = subject

    def check_student(self, student):
        print("Перевірка студента:")
        print(student.get_info())

    def get_teacher_info(self):
        return f"Викладач предмету: {self.subject}"

student1 = Student("Лотошинський Роман", 2, 66)
monitor1 = Monitor("Кава Анастасія", 2, 89, "КН-21")
teacher1 = Teacher("Іваць Максим", 2, 58, "Python")

print(student1.get_info())
print(monitor1.get_monitor_info())
print(teacher1.get_teacher_info())

teacher1.check_student(monitor1)

print(Student.get_count())

print(isinstance(monitor1, Monitor))
print(isinstance(monitor1, Student))

print(issubclass(Monitor, Student))
print(issubclass(Teacher, Student))
