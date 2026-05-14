### Львівський національний університет ветеринарної медицини та біотехнологій імені С.З. Ґжицького

### Звіт про виконання лабораторної роботи

## На тему "Основи процедурного програмування в Python 3"
Виконав студент групи КН-21 Пакуля Артем

Прийняв доц. Андрій Татомир

### Львів 2026

---

**Мета роботи** Мета роботи полягає у засвоєнні студентами методів та прийомів роботи з 
функціями.   

# Лабораторна робота №4

## Хід роботи

1. У ході виконання завдання з функціями було розроблено програму для виводу
```python
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
```
Результат:
(image/function.png)

## Висновки
Під час виконання цієї лабораторної роботи я навчився створювати та викликати функції.
