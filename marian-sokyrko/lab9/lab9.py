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
            print(
                f"Контрактник {self.last_name} та бюджетник {budget_student.last_name} навчаються на {self.course} курсі.")


if __name__ == "__main__":
    student1 = Student("Мар'ян", "Сокирко", 2, 75)
    student2 = Student("Орест", "Баган", 2, 90)
    student3 = Student.from_string("Максим, Іваць, 2, 85")
    student4_b = BudgetStudent("Данило", "Кудла", 2, 95, 3000)
    student5_c = ContractStudent("Олег", "Борисенко", 2, 73, 30000)

    all_students = [student1, student2, student3, student4_b, student5_c]
    for student in all_students:
        print(student)

    print(Student.get_total_students())
    print(f"Чи у Ореста ({student2.average_score}) бал вищий ніж у Максима ({student3.average_score})?")
    print(f"Результат (student2 > student3): {student2 > student3}")
    print(f"\nЧи у Данила ({student4_b.average_score}) бал нижчий ніж у Олега ({student5_c.average_score})?")
    print(f"Результат (student4_b < student5_c): {student4_b < student5_c}")