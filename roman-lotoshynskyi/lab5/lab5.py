class Student:
    def __init__(self, name, course, score):
        self.name = name
        self.course = course
        self.score = score

    def get_info(self):
        return f"Студент: {self.name} Курс: {self.course} Середній бал: {self.score}"

student1 = Student("Лотошинський Роман", 2, 68)
student2 = Student("Іваць Максим", 2, 75)
print(student1.get_info())
print(student2.get_info())