### Львівський національний університет ветеринарної медицини та біотехнологій імені С.З. Ґжицького

### Звіт про виконання лабораторної роботи

## На тему "Налаштування середовища розробки Python 3 і запуск програм"
Виконав студент групи КН-21 Пакуля Артем

Прийняв доц. Андрій Татомир

### Львів 2026

---

**Мета роботи** метою роботи є вивчення основ розробки додатків на Python 3.  

# Лабораторна робота №2

## Хід роботи
1. У ході виконання роботи зі змінами та типами даних було виконано завдання.
```python
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
```
Результат:
(images/variables.png)
2. У ході виконання роботи з базовими операціями та приведення типів було виконано завдання.
```python
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
```
Результат:
(images/variables.png)
3. У ході виконання робити зі списками та операціями над ними було виконано завдання.
```python
numbers = [1, 2, 3]
strings = ["hi", "I love Python "]
names = ["John", "Eric", "Jessica"]
second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
```
Результат:
(images/variables.png)
4. У ході виконання робити зі списками і операціями надними було виконано завдання.
```python





