

def Calc(var_1, sign, var_2, ):
    if sign == '*':
        result = var_1 * var_2
    elif sign == '/':
        result = var_1 / var_2
    elif sign == '+':
        result = var_1 + var_2
    elif sign == '-':
        result = var_1 - var_2
    return result


operations = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y}

op = '+'
n1, n2 = 25, 6

print(operations[op](n1, n2))
