l=[]
n=int(input("enter number of list elements:"))
count=0
for t in range(n):
    t=int(input("enter list elements:"))
    if(t%2==0):
        count=count+1
        print('it is even')
print(count)
