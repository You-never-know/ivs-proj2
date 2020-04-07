import math_lib as m

amount=0 # N
sum_normal=0 # x
sum_square=0 # xi

while True:
    try:
        number=float(input())
        amount=m.addition(amount,1)
        sum_normal=m.addition(sum_normal,number)
        sum_square=m.addition(sum_square,(m.multiplication(number,number)))
    except EOFError:
        break


sum_normal=m.multiplication(sum_normal, (m.division(1,amount))) # 1/N * (sum x)

result=m.multiplication(sum_normal,sum_normal) # x^2 
result=m.multiplication(result,amount) # N*x^2

result=m.substraction(sum_square,result) # (sum (xi^2)) - (N*x^2)

help=m.substraction(amount,1) # N - 1
help=m.division(1, help) # 1/(N-1)

result=m.multiplication(help, result) # (1/(N-1)) * ((sum (xi^2)) - (N*x^2))
result=m.root(2,result) 
print (result)
