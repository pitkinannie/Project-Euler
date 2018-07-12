# Amicable numbers
# Problem 21


def d(n):
    s=1
    sqN = int((n ** (1/2.0)) + 1)
    for i in range(2, sqN):
        while(n % i == 0):
            s += i
            if(i == n / i):
                break
            else:
                s += (n / i)
            break
    return(s)
    

ap=0

for j in range(1,10000):
    a = d(j)
    b = d(a)
    if(b == j and j != a):
        ap += a + b
print(ap/2)
