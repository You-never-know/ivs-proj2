#!/usr/bin/env python
# coding: utf-8 
# Implementation of basic math functions 

## The addition operation
# @note \f$ x1\+x2 \f$
# @param x1 First addend
# @param x2 Second addend
# @return The summation
def addition(x1, x2):
	return x1 + x2

## The substraction operation
# @note \f$ x1\-x2 \f$
# @param x1 The minuend
# @param x2 The subtrahend
# @return The difference
def substraction(x1,x2):
	return x1 - x2

## The multiplication operation
# @note \f$ x1\*x2 \f$
# @param x1 The multiplier
# @param x2 The multiplicand
# @return The product
def multiplication(x1,x2):
	return x1 * x2

## The division operation
# @note \f$ x1\/x2 \f$
# @param x1 The numerator
# @param x2 The denominator
# @return The fraction
def division(x1, x2):
    if x2==0:
        return None
    else:
        return x1/x2

## factorial of a non-negative integer x, denoted by x!, is the product of all positive integers less than or equal to x
# @note x!
# @param x Number t
# @return a to the power of x
# @return If x is float return None
# @return If x is less than 0 return None
def factorial(x):
    if (x < 0):
        return None
    if ( x == 0 ):
        return 1
    if ( isinstance(x,float) ):
        return None
    res = 1
    for i in range(1,x+1):
        res = res * i
    return res

## When x is a positive integer, exponentiation corresponds to repeated multiplication n-times (equal to the value of exponent)
# @note \f$ x^exponent \f$
# @param x Number that will be power
# @param exponent N-th power
# @return x to the power of exponent
def exponencial(x, exponent):
    if (x == 0):
        return None
    if (exponent % 1 != 0 ):
        return None
    if (exponent < 0):
        return None
    else:
        return (x)**(exponent)

## N-th roots are treated as special cases of exponentiation, where the exponent is a fraction \f$ \frac{1}{n} \f$
# @note \f$ \sqrt[n]{a} \f$
# @param a Root
# @param n N-th root
# @return[float] N-th root of number a 
def root(x, base):
    if (x == 0):
        return None
    if (base == 0):
        return None
    if ( base < 0):
        if (x < 0):
            return None
        if ( x % 2 == 0):
            return None
    return (base)**(1/x)

## The modulo function finds the remainder after division of a number by another number.
# If x1 is negative number modulo works with absolute value of x1
# If x2 is negative the result is negative value of modulo with positive x2
# @note \f$ x1\%x2 \f$
# @param x1 Divident
# @param x2 Divisor
# @return Remainder after division
def modulo(x1, x2):
    if ( (x2) == 0 ):
        return None
    if ((x1) < 0 ):
        x1=abs(x1)
    if ( (x2) < 0):
        return -( (x1) % (abs(x2)) )
    return (x1)%(x2)

## The negation changes the value of negative number to positive and the other way around
# @note !x
# @param x Number that will be negated
# @return Negated value
def neg(x):
    return -x

## The multiplicative inverse of a fraction (a/b is b/a).
# @note \f$ x^-1 \f$
# @param x Number that is be inverted
# @return Inverted value
def inverse(x):
    if ( (x) == 0 ):
        return None
    else:
        return 1/(x)
