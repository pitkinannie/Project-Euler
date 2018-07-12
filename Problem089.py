# WIP

# Problem 55
# Roman Numerals
rn = ['MMMMDCLXXII', 'MMDCCCLXXXIII', 'MMMDLXVIIII', 'MMMMDXCV', 'DCCCLXXII', 'MMCCCVI', 'MMMCDLXXXVII', 'MMMMCCXXI', 'MMMCCXX', 'MMMMDCCCLXXIII', 'MMMCCXXXVII', 'MMCCCLXXXXIX', 'MDCCCXXIIII', 'MMCXCVI', 'CCXCVIII', 'MMMCCCXXXII', 'MDCCXXX', 'MMMDCCCL', 'MMMMCCLXXXVI', 'MMDCCCXCVI', 'MMMDCII', 'MMMCCXII', 'MMMMDCCCCI', 'MMDCCCXCII', 'MDCXX', 'CMLXXXVII', 'MMMXXI', 'MMMMCCCXIV', 'MLXXII', 'MCCLXXVIIII', 'MMMMCCXXXXI', 'MMDCCCLXXII', 'MMMMXXXI', 'MMMDCCLXXX', 'MMDCCCLXXIX', 'MMMMLXXXV', 'MCXXI', 'MDCCCXXXVII', 'MMCCCLXVII', 'MCDXXXV', 'CCXXXIII', 'CMXX', 'D']
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
final = z = ''
count = total = originalLength = finalLenght = charSaved = 0

'''Numerals must be arranged in descending order of size.
M, C, and X cannot be equalled or exceeded by smaller denominations.
D, L, and V can each only appear once.'''


for j in range (0, 43):
    #calculates value of roman numeral read in
    z = rn[j]
    originalLength = len(z)
    
    i = z.count("I")
    v = z.count("V")
    x = z.count("X")
    l = z.count("L")
    c = z.count("C")
    d = z.count("D")
    m = z.count("M")
    
    total = i*I + v*V + x*X + l*L + c*C + d*D + m*M

#    print("\nRoman numeral " + str(z) + " equals " + str(total))
#    print(z)
    
    #thousands
    y = total
    if(y / 1000 >= 1):
        m = y/1000
        final += "M" * m

    #hundreds
    if( (y / 100) % 10 == 9):
        final += "CM"
    elif((y / 100) % 10 >= 5):
        final += "D"
        c = ((y / 100) % 10) - 5
        final += "C" * c
    elif((y / 100) % 10 == 4):
        #c = (y / 100) % 10
        final += "CD" 
    elif((y / 100) % 10 >= 1):
        c = (y / 100) % 10
        final += "C" * c
    
    #tens
    if( (y / 10) % 10 == 9):
        final += "XC"
    elif((y / 10) % 10 >= 5):
        final += "L"
        x = ((y / 10) % 10) - 5
        final += "X" * x
    elif((y / 10) % 10 == 4):
        #c = (y / 10) % 10
        final += "XL" 
    elif((y / 10) % 10 >= 1):
        x = (y / 10) % 10
        final += "X" * x
    
    #ones
    if(y % 10 == 9):
        final += "IX"
    elif(y % 10 >= 5):
        final += "V"
        i = (y % 10) - 5
        final += "I" * i
    elif(y % 10 == 4):
        final += "IV" 
    elif(y % 10 >= 1):
        x = y % 10
        final += "I" * i
    
    finalLength = len(final)
    charSaved += (originalLength - finalLength)
    print(final)

    
    total = finalLength = originalLength = 0
    final = ''
print(charSaved)
