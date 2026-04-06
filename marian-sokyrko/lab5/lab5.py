class Student:
    def __init__(self, first_name, last_name, course, average_score):
        self. first_name = first_name
        self.last_name = last_name
        self.course = course
        self.average_score = average_score

        self.full_name = f"{first_name} {last_name}"

    def get_description(self):
        return f" Студент {self.full_name}, курс {self.course}, середній бал {self.average_score} "

student1 = Student ("Мар'ян", "Сокирко", 2, 75)
student2 = Student ("Орест", "Баган", 2, 90)

print(student1.get_description())
print(student2.get_description())
