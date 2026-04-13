class Cat():
    def __init__(self,name,breed,age):

        self.name=name
        self.breed=breed
        self.age=age
    def information(self):
        return {"Ім'я" : self.name,
                "Порода" :self.breed,
                "вік" : self.age}
animal1=Cat("буся","британський","3")
animal2=Cat("Вася","британський","3")
print(animal1.information())
print(animal2.information())

