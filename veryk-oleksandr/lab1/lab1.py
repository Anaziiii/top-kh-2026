def pow(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / pow(base, -exponent)
    else:
        result = 1
        for i in range(exponent):
            result *= base
        return result
    

print(pow(2, 3)) 
print(pow(5, -2))
print(pow(3, 0))


