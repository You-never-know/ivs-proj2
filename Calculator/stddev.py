#!/usr/bin/env python
# coding: utf-8
# Autor: Daniel Marek <xmarek72>

# Lincense: GNU GPL v.3 
# Whole licence can be found at https://www.gnu.org/licenses/gpl-3.0.htm

#Copyright (C) 2020  Daniel Marek
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>

import math_lib as m

amount=0 # N
sum_normal=0 # x
sum_square=0 # xi

def load_data():

    while True:
        try:
            numbers=input()

            # if all numbers are on a new line
            try:
               num2=float(numbers)
               calculate_line(num2)

            except ValueError:
               process_line(numbers)
            
        except EOFError:
            break

def process_line(line):

        list1 = line.strip().split(" ")
        list2 = line.strip().split(",")
       
        # if numbers are split by space
        for i in list1:
            try:
               num = float(i) 
               calculate_line(num)

            except ValueError: 
                break

        # if numbers are split by coma 
        for j in list2:
            try:
                num1 = float(j)
                calculate_line(num1)

            except ValueError:
                break


def calculate_line(num):
     global amount, sum_normal, sum_square

     amount=m.addition(amount,1)
     sum_normal=m.addition(sum_normal,num)
     sum_square=m.addition(sum_square,(m.multiplication(num,num)))


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