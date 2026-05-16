class Student:
    student_count = 0

    def __init__(self, first_name, last_name, course, average_score):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self._average_score = average_score
        self.full_name = f"{first_name} {last_name}"
        Student.student_count += 1

    @property
    def average_score(self):
        return self._average_score

    @average_score.setter
    def average_score(self, new_score):
        if 0 <= new_score <= 100:
            self._average_score = new_score
        else:
            print(f"[Помилка валідації]: Неможливо встановити бал {new_score}. Оцінка має бути в межах від 0 до 100!")

    @average_score.deleter
    def average_score(self):
        print(f"[Deleter]: Середній бал студента {self.full_name} було скинуто.")
        self._average_score = 0

    def get_description(self):
        return f"Студент {self.full_name}, курс {self.course}, середній бал {self.average_score}"

    def __str__(self):
        return self.get_description()

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_score > other.average_score
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_score == other.average_score
        return NotImplemented

    @classmethod
    def get_total_students(cls):
        return f"Загальна кількість студентів: {cls.student_count}"

    @classmethod
    def from_string(cls, student_str):
        first_name, last_name, course, average_score = student_str.split(",")
        return cls(first_name.strip(), last_name.strip(), int(course), float(average_score))

    @staticmethod
    def is_passing_grade(grade):
        return grade >= 60

class BudgetStudent(Student):
    def __init__(self, first_name, last_name, course, average_score, scholarship):
        super().__init__(first_name, last_name, course, average_score)
        self.scholarship = scholarship

    def get_description(self):
        return f"[Бюджет] {super().get_description()}, стипендія {self.scholarship}"

class ContractStudent(Student):
    def __init__(self, first_name, last_name, course, average_score, payment_amount):
        super().__init__(first_name, last_name, course, average_score)
        self.payment_amount = payment_amount

    def get_description(self):
        return f"[Контракт] {super().get_description()}, оплата {self.payment_amount}"

    def compare_with_budget(self, budget_student):
        if isinstance(budget_student, BudgetStudent):
            print(f"Контрактник {self.last_name} та бюджетник {budget_student.last_name} навчаються на {self.course} курсі.")

if __name__ == "__main__":

    student1 = Student("Мар'ян", "Сокирко", 2, 75)
    print("Початковий стан:")
    print(student1)
    print("\n--- 1. Тестуємо Getter (@property) ---")
    print(f"Зчитано через getter: {student1.average_score}")
    print("\n--- 2. Тестуємо Setter (Коректне значення) ---")
    student1.average_score = 95
    print(f"Новий бал після зміни: {student1.average_score}")
    print("\n--- 3. Тестуємо Setter (Спроба записати некоректне значення) ---")
    student1.average_score = 120
    print(f"Бал залишився незмінним: {student1.average_score}")
    print("\n--- 4. Тестуємо Deleter ---")
    del student1.average_score
    print(f"Стан студента після роботи deleter-а: {student1}")
