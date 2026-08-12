L=[90,92,67,45,98,54,56,78,76,65]
L[1]=56
total=0
avg=0
print(90 in L)
for i in L:
    total=total+i
avg=total/10
print(avg)
L.append(49)
print(L)
