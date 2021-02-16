for val in "string":
    if val== "i":
        break
    print(val)
print("End")

fruits= ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x== "banana":
        break
num=int(input('Enter the number of factorial:'))
product=1
for i in range(1,num+1):
     product= product*i
print(f'The factorial of {num} is {product}')

num=int(input('Enter the number of factorial:'))
product=1
for i in range(num,0,-1):
     product= product*i
print(f'The factorial of {num} is {product}')

num=int(input('Enter the number of factorial:'))
product=1
for i in range(1,11):
     product= num*i
     print(f'The factorial of {num} is {product}')