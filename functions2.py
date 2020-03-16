# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 07:30:06 2019

@author: alexius
"""

#with functions 
#the scope of a programm is a part of the program where that variable is accessible

#varibles defined outside of function are said to be withing the 'Gllobal Scope' they can be accessed anywhere after they've been defined

#variable defined in Global scope is called Global variable

#in simple terms, you can define your parameter at any time and call the unction
#that ariable is kept

#variables in local scope are not kept

#if no local variable defined, the function runs and searches for gloabl variable

#can put 'global' when defining funcvion to highlight its a global variable

def mult():
    global x
    print(x)

x=24
x=34    
mult () # prints value of x defined globally
    
    