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
        return f"Кількість створених об'єктів: {cls.count}"


student1 = Student("Лотошинський Роман", 2, 68)
student2 = Student("Іваць Максим", 2, 76)
student3 = Student("Кава Анастасія", 2, 95)
print(student1.get_info())
print(student2.get_info())
print(student3.get_info())
print(Student.get_count())