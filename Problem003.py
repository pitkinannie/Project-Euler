# Problem 3
# Largest prime factor

def mpf(n):
    p = -1
    
    while(n % 2 == 0):
        p = 2
        n /= 2
    
    sqN = n ** (1/2) + 1
    sqN = int(sqN)
    for i in range(3, sqN, 2):
        while(n % i == 0):
            p = i
            n /= i
            
    if n > 2: 
        p = n
        
    return(int(p))
    
print(mpf(600851475143))
