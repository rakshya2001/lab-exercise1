num=int(input('Enter the number'))
if num<0:
    print('Number is negative')
print('Program is over')
#in case of even
num=int(input('Enter the number'))
if num%2==0:
    print('Number is even')
else:
    print('Number is odd')
print('Program is over')
#number is zero
num=int(input('Enter the number'))
if num==0:
    print('Number is zero')
print('the program is over')
#num is positive or negative
num=int(input('Enter the number'))
if num>0:
    print('Number is positive')
else:
    print('Number is negative')
#elif
num=int(input('Enter the number'))
if num==1:
    print('Sunday')
elif num==2:
    print('Monday')
elif num==3:
    print("Tuesday")
elif num==4:
    print('Wednesday')
elif num==5:
    print('Thursday')
elif num==6:
    print('Friday')
elif num==7:
    print('Saturday')
print('program is over')
#write a program to take a input from the user, ask the user age. If asathe user age is below 15 , print a message
# "You are a child", if the users age is greater than 15 and lesser than 40, print a message "You are adult",
# if the users age is greater than 40 then print a message "you are old"
age=int(input('Enter the age'))
if age<15:
    print('You are a child')
elif age<15 and age>40:
    print('You are adult')
elif age>40:
    print('You are old')
print('program is over')
# A person has a basic salary 20,000,he spent 10% of his basic salary as expenses.Write a program to find gross net
#salary after his expenses
salary==20000
expenses==10/100*(20000)
gross net salary=salary-expenses
