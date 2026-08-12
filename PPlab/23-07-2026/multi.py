'''
Multiplication table of n is
   nx1=n
   nx2=2*n
   nx3=3*n
   .
   .
   .
   nx10=10*n
'''

#n=int(input('Enter any number'))

i=1
num=1
while num<=20:
    while(i<=10):
        print(f"Mltiplication table  is {num}*{i}={num*i}")
        i=i+1
    num=num+1

