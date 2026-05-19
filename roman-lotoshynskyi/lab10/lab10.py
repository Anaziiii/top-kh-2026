class Student:
    def __init__(self, name, course, score):
        self._name = name
        self._course = course
        self._score = score

    # getter
    @property
    def score(self):
        return self._score

    # setter
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self._score = value
        else:
            print("Некоректний бал! Має бути від 0 до 100.")

    # deleter
    @score.deleter
    def score(self):
        print("Оцінку видалено")
        self._score = None

    def get_info(self):
        return f"Студент: {self._name}, Курс: {self._course}, Середній бал: {self._score}"


student1 = Student("Лотошинський Роман", 2, 68)
student2 = Student("Іваць Максим", 2, 75)

print(student1.get_info())
print(student2.get_info())

student1.score = 95  # правильне число балів
student2.score = 101  # неправильне число балів
del student2.score

print(student1.get_info())
print(student2.get_info())