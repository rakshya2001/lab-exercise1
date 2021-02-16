i=1;
while i<=10:
    print(i)
    i +=1
#for reverse
i=10;
while i>=1:
    print(i)
    i -=1
#chosing game

#import random

#number=random.randint(1,10)
#guess=int(input('please guess the number?'))
#while number!=guess:
   # guess=int(input('oops !!  try again: guess again:'))
#else:
   # print('Congratulations!!! You are right')


import random

number=random.randint(1,10)

while True:
    guess= int(input("Please guess the number?"))
    if guess==number:
        print('La badhai chaa')
        break
    print("oops!!try agaain:")