'''Here We are finding the largest 
collatz sequence among 1 to 100 numbers'''
num=1
max_len=1
max_num=1
while num<=999:
    n=num
    length=1
    while(n!=1):
        if(n%2==0):
            n=n//2
        else:
            n=3*n+1
        length=length+1
    print("It follows collatz conjecture")
    print(f'{length} is the length of the sequence')
    if length>max_len:
        max_len=length
        max_num=num
    num=num+1
print(f"maximum collatz length {max_len} for {max_num}")

