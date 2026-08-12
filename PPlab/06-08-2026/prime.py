primelist=[]
def is_primenumber(n):
    sqrt=int(n**0.5)
    for t in range(2,10):
   # for t in range(2,10):
        if t>sqrt:
            return True
        if(n%t==0):
           # count=count+1
            return False
    return True
#x=int(input('enter any number'))
   # if(count<=2):
    #    print(f'{n} is a prime number')
   # else:
   #     print(f'{n} is not a prime number')
x=int(input('enter any number:'))
sqrt=int(x**0.5)

for s in range(2,sqrt+1):
    if is_primenumber(s):
        primelist.append(s)
        print(primelist)

if is_primenumber(x):
   print(f'{x} is prime number')
else:
   print(f'{x} is not a prime number')

