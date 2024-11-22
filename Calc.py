def Calculate(x, y):
    if Type == '+':
        add_result = x + y 
        return add_result

    elif Type == '-':
        sub_result = x - y
        return sub_result 

    elif Type == '*':
        mul_result = x * y
        return mul_result 

    elif Type =='/':
        div_result = x / y
        return div_result 

Num1 = float(input('Enter a number: '))
Num2 = float(input('Enter a number: '))
Type = input('What arithmetic would you like: ')

print(Calculate(Num1, Num2))  
