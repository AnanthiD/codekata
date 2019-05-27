z=input()
count=0
for c in z:
    if (not c.isalnum()):
        count=count+1
print(count)