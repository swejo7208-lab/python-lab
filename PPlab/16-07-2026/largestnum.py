a=int(input('Enter 1st integer'))
b=int(input('Enter 2nd integer'))
c=int(input('Enter 3rd integer'))
if(a>b and a>c):
    print(f'{a} is largest')
elif(b>a and  b>c):
    print(f'{a} is equal to {b}')
else:
    print(f'{b} is largest')


