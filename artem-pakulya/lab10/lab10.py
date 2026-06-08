class Cat:
    def __init__(self, age):
        self._age = age 
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            print("Помилка: Вік не може бути від'ємним!")
        else:
            self._age = value
    @age.deleter
    def age(self):
        print("Інформацію про вік кота видалено!")
        self._age = None
c1 = Cat(3)
print("Поточний вік:", c1.age)
c1.age = 5                      
print("Новий вік:", c1.age)
c1.age = -2                     
del c1.age                     
print("Вік після видалення:", c1.age)