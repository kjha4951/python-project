# square root

'''num1=int(input("enter a number"))
sr=num1**(1/2)
print(f"the square root of {num1} is {sr}")'''

'''import math
num=int(input("enter the number here"))
sr=math.sqrt(num)
print(f"the square root of {num} is {sr}")'''


# find factorial of a number
# 5! = 5*4*3*2*1 = 120 and we can not find the factorial of nagetive values

'''num=int(input("enter the number "))
fact=1
if num<0:
    print("doesn't exist")

if num==0:
    print("factorial of 0 is",1)
if num<0:
 for i in range(1,num+1):
    fact = fact*i

print(f"the factorial of {num} is {fact}")'''


'''def fact(num):
    if num<=0: 
        return 1
    else:
        return (num ) * fact(num-1)

num=int(input("enter the numbet he you want to pass = "))
result=fact(num)
print(f"the factorial of {num} is {result}")'''


#check nagetive positive and zero
'''num=int(input("inter a number -> "))
if num==0:
 print(f"the {num} is zero")
if num<0:
  print(f"the {num} is negative")
if num>0:
   print(f"the {num} is posivit")'''


# prime number

'''num=int(input("enter a number "))
falg=False
if num==1:
    print("this is numt an prime nyymber")
for i in range(2,num):
    if (num%i)==0:
        falg=True

if falg:
    print(f"the {num} is not factorial")
else:
    print(f"the {num} is prime")'''

#palinfrome
def is_palindrome(str):
    str=str.replace(" "," ").lower()
    return str == str[::-1]


str=input("enter the string ")

print(is_palindrome(str))