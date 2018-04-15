################## Python Basics #######################
##### Hello World ###
print ("Hello World")

### Variable and DataType ####
intval = 5
floatval = 6.541
boolval = False
print (boolval)
boolval = True
print (intval)
print (floatval)
print (boolval)

######## Multiply.line ###############
add = 3+9
sub = 9-3
div = 20/2
prod = 5*9

operators1 = 3
operators2 = 3
operators3 = 3

operators1 **= 5
operators2 //= 0.96
operators3 %= 2
print (add , sub, div, prod)
print (operators1 , operators2 , operators3)

############String and print ########
print('single quotes')
print("double quotes")
print(len("Manchester United"))
print(str (12345)[2] )
print("albania".upper())
print("BELGIUM".lower())

##### print Review Exercise #####
name = input ("please Enter Your Name.")
print ("Your Name Is" + "%s" % (name))
####### Flow Control and Comperators Review #######
print (6 > 6)
print (6 <= 6)
print (5 < 5)
print (10 != 10)
print (4 == 5)
print (7 >= 7)
print (7 != 9)
print (5 < 9)
print (20 == 6)
print (5 > 6)
print (3 == 3)
print (2 == 1)
######### If Statement ########
###Example to understand (If - Then - Else - Elif) Condition ####
if 1 == 2:
    print ("Don't print this")     #In this condition  if this True print this word
elif 1 != 2:                       #In this condition if i show the program many offer
    print ("Print This.")
else:                              #In this condition if i want to end the if condition
    print ("Don't print this either.")

### Another Example to overview( Show Opevious ) If Statement Condition ###
if 1 ==2:
    print ("Don't print This")
elif 1 != 2:
    print ("Print This either.")
elif 5 <= 19:
    print ("2nd elif statement.")
else:
    print ("This Will not be printed.")
#############################################################################
### Another Example to If StateMent #####
name = input ("Enter Your Name.")
nameLen = len(name)
if nameLen < 4:
    print ("Your Name is less than 4 characters.")
elif nameLen < 10:
    print ("Your name is at least 4 characters and less than 10 characters.")
else:
    print ("Your name is very long.")
  ############################################################
  ############### Function ########
def mult(a ,b ,c):
    d = a * b
    print(d + c)

mult (2 , 3, 4)
########################
#Another Example###
def giver(a ,b):
    c = a + b
    return c
def taker(d , e):
    output = giver(d , e)
    return output
print (taker (1 , 5))
##### Function Review Exercises #####
def first():
    print ("This is a function.")

def intfun(intval):
    return intval + 2

def takesTwo (int1 , int2):
    return int1 + int2

def functionInsides(a ,b ,c):
    print(takesTwo(intfun(a),b))
first()
functionInsides(7 , 4 , 2)
################################################
########## Important Modules explain to understand it!!!####################
import random
print (random.randint(1,10))
############################
from random import randint
print (randint(10 ,20))
###################################
from random import *
print (random())
#################How it writes in program!!##############
import random
from random import randint
from math import *
print (randint(5 ,10 ))
print (factorial(4))
print (random.random())
#################################
###### List Review Exercises #####
listval = [1 , 2, 3 ,4 ,5 , 6]
print (listval)

listval[4] = [5]
print (listval)

listval.append(7)
print (listval)

print (listval[:4])
print (listval[2:5])
print (listval[5:])
print (listval.index(7))

listval.insert(0 , 0)
print (listval)

listval.removed (3)
print (listval)

print (listval.pop())
print (listval)
#############################################
################# While Loops ##################
counter = 0
while counter < 5:
    print ("some thing ")
    counter += 1
    ###############Another Example ##################
counter = 1
while True :
    print ("Here's Jonnny !!!")
    counter += 1
    if counter > 5:
        break
 ###########################
 ###While Else ###########
while counter < 5:
    print(counter)
    counter += 1
else:
    print (5)
######################################################
##############Try & Except ###################
def divide (top , bottom):
    try:
        print (top / bottom)
    except ZeroDivisionError:
        print ("You can't divide by 0")
    divide("mushroom",True)
#####################################################






















