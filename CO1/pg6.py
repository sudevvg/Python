li = []
c = 0
for i in range(3):
    x = input("enter names:")
    li.append(x)
for i in li:
    for j in i:
        if 'a' in j:
            c = c + 1
print("number of a is:", c)
