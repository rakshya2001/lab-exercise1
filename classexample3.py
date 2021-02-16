
    #print(i,end=' ')

for i in range(4):
    for i in range(4):
        print('*',end=' ')
    print()

for i in range(2):
    for i in range(3):
        print('2',end=' ')
    print()
#another
for i in range(4):
    for j in range(i+1):
        print('*',end=' ')
    print()
#another
for i in range(4):
    for j in range(i+1):
        print(i+1,end=' ')
    print()
#another
num=0
for i in range(4):
    for j in range(i+1):
        print(num,end=' ')
        num+=1
    print()

