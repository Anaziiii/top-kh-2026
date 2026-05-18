class Student:
    def __init__(self, name, course, score):
        self.name = name
        self.course = course
        self.score = score

    def get_info(self):
        return f"Студент: {self.name} | Курс: {self.course} | Бал: {self.score}"

    def __str__(self):
        return self.get_info()

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score


class BudgetStudent(Student):
    def get_info(self):
        return f"[Бюджет] {self.name} | Курс: {self.course} | Бал: {self.score}"


class ContractStudent(Student):
    def get_info(self):
        return f"[Контракт] {self.name} | Курс: {self.course} | Бал: {self.score}"


student1 = BudgetStudent("Лотошинський Роман", 2, 67)
student2 = ContractStudent("Іваць Максим", 2, 74)

# поліморфізм
print(student1.get_info())
print(student2.get_info())

# магічні методи
print(student1)  # __str__
print(student1 < student2)  # __lt__
print(student1 == student2) # __eq__