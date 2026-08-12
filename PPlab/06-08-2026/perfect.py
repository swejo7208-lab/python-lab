# to check wherther the given number is either perfect number or not
def is_perfectnumber(n):
    sof=0
    for i in range(1,n+1):
        if(n%i==0):
            sof=sof+i
    if sof==2*n:
        return True
    else:
        return False
#x=int(input('Enter a number'))
for x in range(1,10001):
    if is_perfectnumber(x):
        print(f'{x} is a perfect number')
    #else:
        #print(f'{x} is not a perfect number')
