### Львівський національний університет ветеринарної медицини та біотехнологій імені С.З. Ґжицького

### Звіт про виконання лабораторної роботи

## На тему "Основи структурного програмування в Python 3"
Виконав студент групи КН-21 Пакуля Артем

Прийняв доц. Андрій Татомир

### Львів 2026

---

**Мета роботи** ознайомлення основними прийомами структурного програмування у Python 3.   

# Лабораторна робота №3

## Хід роботи
1. У ході виконання завдання з умовними операторами.
```python
number = 20
second_number = None
first_array = [1,4,5]
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
(images/operators.png)

2. У ході виконання завдання з циклами **for and while** було взято завдання з сайту (https://www.w3schools.com/).
```python
fruits=["apple", "banana", "cherry"]
for i in fruits:
    print(i)
    if i == "banana":
        break
```
Результат:
(images/for.png)

```python
i=0
while i<6:
    i+=1
    if i == 3:

        continue
    print(i)
```
Результат:
(images/while.png)

## Висновки
Під час виконання цієї лабораторної роботи я навчився працювати з умовними операторами та циклами.


