flag = True
while flag:
    try:
        res = eval(input('Введіть математичний вираз: '))
        print(res)
    except:
        print("Невірно вписаний вираз!")
    ask = input("Спробувати ще раз? (y|n) ")
    if ask.lower() == 'y':
        continue
    else:
        flag = False
        