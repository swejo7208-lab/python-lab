A=input("enter any string")
vowels="AEIOUaeiou"
count=0
for c in A:
    if c in vowels:
        count=count+1
print(count)

