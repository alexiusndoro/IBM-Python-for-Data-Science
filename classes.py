# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 08:16:09 2019

@author: alexius
"""

import matplotlib as plt
#
#you can find the type of object we have using type()

#the type o object is aka the instance of that type


#classes  have data attributes and methds

# use the following syntax:
#   class NameofClass (object):

#the function init tells python you're making  a new classs
#it initializes data attributes

#self represents the instance of the class.
# By using the “self” keyword we can access the attributes and methods of the class in python.
# It binds the attributes with the given arguments.
# self is parameter in function and user can use another parameter name in place of it.

#self contains all attributes in the set 

#constructor
class rectangle(object):
    def __init__(self,length,width):
        self.length =  length
        self.width = width
#method
        
    def addlength(self,l): #method to increase legnth of rectangle
        self.length = self.length + l
        return self.length
#method
    def drawRectangle1(self):
        plt.pyplot.gca().add_patch(plt.patches.Rectangle((0, 0), self.length, self.width ,fc="cyan"))
        plt.axis('scaled')
        plt.show()

'''    def drawRectangle(self):
        plt.pyplot.gca().add_patch(plt.patches.Rectangle((0, 0), self.length,self.width,fc="cyan"))
        plt.axis('scaled')
        plt.show()  
        '''


#think of self as a ox which contains the attributes of each class
r1 = rectangle(24,20)

print (r1.length) #prints normal rectangle
#can change the attribute values of the instances e.g.
r1.length = 5
print(r1.length)

#using the addlwength method method
r1 = rectangle(24,20)
print (r1.addlength(30)) #prints rectangle with added length

#using the drawing method
r1.drawRectangle1()

#use dir(yourObject) to see the methods of the class


        