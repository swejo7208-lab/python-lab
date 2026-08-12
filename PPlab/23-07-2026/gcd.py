'''
GCD of two numbers using Euclid's Algorithm

a=b.q+r
if r=0,then b is gcd
otherwise gcd of b,r

'''
a=int(input('Enter First integer'))
b=int(input('Enter Second integer'))
while True:
    r=a%b
    if(r==0):
        print('gcd is',b)
        break
    else:
        a=b
        b=r
