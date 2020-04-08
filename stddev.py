import math_lib as m

amount=0 # N
sum_normal=0 # x
sum_square=0 # xi

def load_data():
    global amount, sum_normal, sum_square

    while True:
        try:
            numbers=input()

            # if all numbers are on a new line
            try:
               num2=float(numbers)
               amount=m.addition(amount,1)
               sum_normal=m.addition(sum_normal,num2)
               sum_square=m.addition(sum_square,(m.multiplication(num2,num2)))
            except ValueError:
               process_line(numbers)
            
        except EOFError:
            break

def process_line(line):
        global amount, sum_normal, sum_square

        list1 = line.strip().split(" ")
        list2 = line.strip().split(",")
       
        # if numbers are split by space
        for i in list1:
            try:
               num = float(i) 
               amount=m.addition(amount,1)
               sum_normal=m.addition(sum_normal,num)
               sum_square=m.addition(sum_square,(m.multiplication(num,num)))
            except ValueError: 
                break

        # if numbers are split by coma 
        for j in list2:
            try:
                num1 = float(j)
                amount=m.addition(amount,1)
                sum_normal=m.addition(sum_normal,num1)
                sum_square=m.addition(sum_square,(m.multiplication(num1,num1)))
            except ValueError:
                break



def calculate_result():
    global amount, sum_normal, sum_square,result

    sum_normal=m.multiplication(sum_normal, (m.division(1,amount))) # 1/N * (sum x)

    result=m.multiplication(sum_normal,sum_normal) # x^2 
    result=m.multiplication(result,amount) # N*x^2

    result=m.substraction(sum_square,result) # (sum (xi^2)) - (N*x^2)

    help=m.substraction(amount,1) # N - 1
    help=m.division(1, help) # 1/(N-1)

    result=m.multiplication(help, result) # (1/(N-1)) * ((sum (xi^2)) - (N*x^2))
    result=m.root(2,result) 
    
load_data()
calculate_result()
print(result)