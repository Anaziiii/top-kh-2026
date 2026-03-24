Львівський національний університет ветеринарної медицини та біотехнологій імені С.З. Ґжицького

Кафедра інформаційних технологій

# Звіт про виконання лабораторної роботи №3
на тему: "Основи структурного програмування в Python 3"

Виконав студент групи КН-21 Баган Орест

Прийняв доц. Андрій Татомир

### Львів 2026

---

**Мета роботи** – ознайомлення основними прийомами структурного
програмування у Python 3.

## Хід роботи

1. У ході виконання даної роботи ознайомився з оператором **if**
Код:
```python

number = 16
second_number = None
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
```

Результат:

![код](/orest-bagan/lab3/lab3-img/operators.png)

2. Освоїм основу роботи з циклом **for** (завдання з сайту w3school)
Код:
```python

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

```

Результат:

![код](/orest-bagan/lab3/lab3-img/for.png)

2. Робота з циклом **while** (завдання з сайту w3school)
Код:
```python

i = 0
while i < 6:
    if i != 3:
        print(i)
    i += 1


```

Результат:

![код](/orest-bagan/lab3/lab3-img/while.png)

## Висновки
У результаті виконання даної роботи було ознайомлено з принципом роботи операторів **if** та **else**, а також циклами **for** і **while**