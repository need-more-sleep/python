#!/usr/bin/env python
# coding: utf-8

# In[2]:


# -*- coding: utf-8 -*-

def plus(a,b):
    return a+b

def mius(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    return a//b

while (True):
    
    print(' ** 간단 계산기 ** ')
    print( ' 종료 하려면 : 0  ')
    print(' ***************** ')
    
    number1 = int(input(' 첫번째 수  : '))
    
    if number1==0:
        print( ' good bye ')
        break
        
    oper = str(input(' + -, *, / : '))
    
    number2 = int(intpu(' 두번째 수 : '))
    
    
    if( oper == '+'):
        res = plus(number1, number2)
        
    elif oper == '-':
        res = minus(number1, number2)
        
    elif oper == '*':
        res = multi(number1, number2)
        
    elif oper == '/':
        res = divi(number1,number2)
        
    else:
        print(' {} 연산자 없음 '.format(oper))
        
    print(' 결과 : {} {} {} = {} '.format(number1, oper, number2, res))

