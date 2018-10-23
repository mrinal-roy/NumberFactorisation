#! usr/bin/env python3

def isPrime(checkNum):   #Function isPrime to check if Prime Number or Not a Prime Number
    PRIMECOND = False
    if (checkNum == 1) or (checkNum == 2) or (checkNum == 3):
        PRIMECOND = True
    elif checkNum > 3:    
        for i in range(2,checkNum,1):
            rem = checkNum % i
            if rem != 0:
                PRIMECOND = True
            else:
                PRIMECOND = False
                break

    return PRIMECOND

print('This program finds the Factors as well as the Prime Factors\
of a Number and Checks if the Number is a Prime Number')
print("Enter the Number whose Factors you want to find:")
num = int(input())   #user input of the Number

factor = []

for k in range(1,num+1):   # finding Factors of the Number
    REM = num % k
    if REM == 0:
        factor.append(k)

    else:
        continue
primeFactor = []
for eachFactor in factor:   # finidng the Prime Factors of the Number
    if isPrime(eachFactor):
        primeFactor.append(eachFactor)
    else:
        continue
print('The factors of ' + str(num) + ' are as follows: '+ str(list(factor)))
print('The prime factors of '+ str(num) + ' are as follows: '+ str(list(primeFactor)))

if (len(primeFactor) == 2) or (factor == primeFactor):
    print('Number ' + str(num) + ' is a Prime Number')
else:
    print('Number ' + str(num) + ' is a Not Prime Number')

