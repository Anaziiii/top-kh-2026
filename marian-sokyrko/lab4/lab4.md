Львівський національний університет ветеринарної медицини та біотехнологій імені С.З. Ґжицького

Кафедра інформаційних технологій

# Звіт про виконання лабораторної роботи №4
на тему: "Основи процедурного програмування в Python 3"

Виконав студент групи КН-21 Сокирко Мар'ян

Прийняв доц. Андрій Татомир

### Львів 2026

---

**Мета роботи** - полягає у засвоєнні студентами методів та прийомів роботи з функціями.

## Хід роботи

1. Під час виконання лабораторної роботи я ознайомився з функціями *def*

Код:
```python
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
```

Результат:

![function.png](images/function.png)

## Висновки:

### Висновок
**Виконав:** Сокирко Мар'ян

Під час виконання даної лабораторної роботи я ознайомився з функціями *def*. Також ознайомився з форматом виводу *%s*.