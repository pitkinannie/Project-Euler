# Lychrel numbers
# Problem 55

l = 0
p = False

for j in range(1, 10000): 
    x = 1
    while(p == False):
        i = int((str(j))[::-1])
        s = str(j + i)

        if(s == s[::-1]):
            p = True
        if(x == 50):
            l += 1
            p = True

        x += 1
        j = int(s)

    p = False
print(l)
