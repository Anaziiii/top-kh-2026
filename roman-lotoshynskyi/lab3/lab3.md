Львівський національний університет ветеринарної медицини та біотехнологій імені С.З. Ґжицького

Кафедра інформаційних технологій

# Звіт про виконання лабораторної роботи №3
на тему: "Основи структурного програмування в Python 3"

Виконав студент групи КН-21 Лотошинський Роман

Прийняв доц. Андрій Татомир

### Львів 2026

---

**Мета роботи** – ознайомлення основними прийомами структурного
програмування у Python 3.

## Хід роботи

1. Під час виконання цієї лабораторної роботи я ознайомився з оператором **if**

Код:
```python
number = 18
second_number = 0
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

![код](/roman-lotoshynskyi/lab3/images/operators.png)

2. Освоїв роботу з циклом **for** (завдання взято з сайту W3School)

Код:
```python
fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)
    if i == "banana":
       break
```

Результат:

![код](/roman-lotoshynskyi/lab3/images/for.png)

3. Ознайомився з роботою циклом **while** (завдання взято з сайту w3school)

Код:
```python
i = 0
while i < 6:
   i += 1
   if i == 3:
      continue
   print(i)
```

Результат:

![код](/roman-lotoshynskyi/lab3/images/while.png)

## Висновки
Під час виконання лабораторної роботи я ознайомився та навчився працювати з принципом роботи операторів **if** та **else**, а також циклами **for** і **while**