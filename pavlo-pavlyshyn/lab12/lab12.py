class DogCard:
    def __init__(self):
        self.name = ""
        self.breed = "невідома"
        self.age = 0
        self.vaccines = []
        self.chipped = False
        self.note = ""

    def __str__(self):
        vaccines = ", ".join(self.vaccines) if self.vaccines else "немає"
        chip = "так" if self.chipped else "ні"
        text = f"Анкета: {self.name}\n"
        text += f"  Порода: {self.breed}\n"
        text += f"  Вік: {self.age}\n"
        text += f"  Щеплення: {vaccines}\n"
        text += f"  Чіп: {chip}"
        if self.note:
            text += f"\n  Примітка: {self.note}"
        return text


# Будівельник збирає анкету крок за кроком
class DogCardBuilder:
    def __init__(self, name):
        self.card = DogCard()
        self.card.name = name

    def set_breed(self, breed):
        self.card.breed = breed
        return self

    def set_age(self, age):
        self.card.age = age
        return self

    def add_vaccine(self, vaccine):
        self.card.vaccines.append(vaccine)
        return self

    def set_chip(self):
        self.card.chipped = True
        return self

    def set_note(self, note):
        self.card.note = note
        return self

    def build(self):
        return self.card


# Директор знає готові "рецепти" анкет
class Registrar:
    def street_dog(self, name):
        builder = DogCardBuilder(name)
        builder.set_note("Знайдена на вулиці, потребує огляду ветеринара")
        return builder.build()

    def ready_for_adoption(self, name, breed, age):
        builder = DogCardBuilder(name)
        builder.set_breed(breed).set_age(age)
        builder.add_vaccine("сказ").add_vaccine("чумка")
        builder.set_chip()
        return builder.build()


registrar = Registrar()
print(registrar.street_dog("Сірко"))
print(registrar.ready_for_adoption("Барс", "Вівчарка", 5))

# Анкету можна зібрати і вручну, без директора
custom = DogCardBuilder("Дуна").set_breed("Вівчарка").set_age(4).add_vaccine("сказ").build()
print(custom)
