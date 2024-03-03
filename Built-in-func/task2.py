string=str(input())
uppercount=0
lowercount=0
for x in string:
    if x.isupper():
        uppercount+=1
    if x.islower():
        lowercount+=1
print(uppercount)
print(lowercount)
