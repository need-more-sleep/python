# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def plus(a,b):
    return a+b

def mius(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    return a//b

while (True):
    
    print(' ** calculate ** ')
    print( ' do you want exit : 0  ')
    print(' ***************** ')
    
    number1 = int(input(' first  : '))
    
    if number1==0:
        print( ' good bye ')
        break
        
    oper = str(input(' + -, *, / : '))
    
    number2 = int(input(' second : '))
    
    
    if( oper == '+'):
        res = plus(number1, number2)
        
    elif oper == '-':
        res = mius(number1, number2)
        
    elif oper == '*':
        res = multi(number1, number2)
        
    elif oper == '/':
        res = divi(number1,number2)
        
    else:
        print(' {} do not have operand '.format(oper))
        
    print(' result : {} {} {} = {} '.format(number1, oper, number2, res))

