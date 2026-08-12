'''Collatz Conjecture or 3n+1 problem
--------------------------------------
The sequence of operations 
if n is even then n/2
if n is odd then 3*n+1
Apply the above operations,any given positive
integer terminates at 1.
7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1
'''

n=int(input('Enter any number:'))
length=1
while(n!=1):
    if(n%2==0):
        n=n/2
        print(n)
    else:
        n=3*n+1
        print(n)
    length=length+1
print('It follows the collatz conjecture')
print(f'{length} is the total length of the sequence')

