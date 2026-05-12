### Львівський національний університет ветеринарної медицини та біотехнологій імені С.З. Ґжицького

### Звіт про виконання лабораторної роботи

## На тему "Вивчення вбудованих типів даних і методів роботи з ними Python 3"
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
(images/basic_operators.png)
3. У ході виконання робити зі списками та операціями над ними було виконано завдання.
```python
numbers = [1, 2]
strings = ["hi", "I love Python "]
names = ["John", "Eric", "Jessica"]
second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
```
Результат:
(images/lists.png)
4. У ході виконання роботи зі словниками та операціями над ними було виконано завдання.
```python
phonebook = {
"John" 938477566,
"Jack": 938377264,
"Jill": 947662781
}
phonebook ["Jake"] = 938273443
del phonebook["Jill"]
if "Jake" in phonebook:
print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
print("Jill is not listed in the phonebook")
```
Результат:
(images/dictionaries.png)
5. У ході виконання роботи зі стрічками було виконано завдання.
````python

s = "Strings are awesome!"
print("Length of s = %d" % len(s))
print("The first occurrence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))
print("The first five characters are '%s'" % s[:5])
print("The next five characters are '%s'" % s[5:10]) 
print("The thirteenth character is '%s'" % s[12]) 
print("The characters with odd index are '%s'" %s[1::2]) 
print("The last five characters are '%s'" % s[-5:])
print("String in uppercase: %s" % s.upper())
print("String in lowercase: %s" % s.lower())

if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

print("Split the words of the string: %s" % s.split(" "))
````
Результат:
(images/string_operations.png)

## Висновки
Під час виконання цієї лабораторної роботи я навчився працювати зі змінними, базовими операціями і типами даних, а також зі списками, словниками та рядками.




