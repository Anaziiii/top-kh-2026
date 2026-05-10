a = 0
b = 0
while True:
    a = int(input("введи перше число: "))
    operator = input("оператор: ")
    b = int(input("введи друге число: "))
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b 
    elif operator == "/":
        if b != 0:
            result = a / b
        else:
            print("на нуль ділити не мож")
            continue
    elif operator == "*":
        result = a * b
    else:
        print("невідомий оператор") 
        continue
    print("результат: ", result)
    c = input("продовжити?(якщо ні напишіть ""ні"") ")
    if c.lower() == "ні": 
        print("бай бай")
        break
    
