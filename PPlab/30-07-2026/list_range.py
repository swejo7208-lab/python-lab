l=[]
n=int(input("enter number of students:"))
tot=0
avg=0
for s in range(n):
    s=int(input("enter score:"))
    l.append(s)
    tot=tot+s
avg=tot/n
print(avg)


