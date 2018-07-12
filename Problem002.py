# Problem 2
# Even Fibonacci numbers

n = i = fSum = 0
f = [1, 2]

while n < 4000000:
    n = f[i] + f[i+1]
    f.append(n)
    i += 1
f.pop(-1)

fSum = 0
for j in range(1, len(f), 3):
    fSum += f[j]

print(fSum)
