# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# Fibbonacci sequence: 1,1,2,3,5,8,13...
curF=1
prevF=1
nextF=0
sumOfEven=0
while(curF <=4000000):
    nextF=curF+prevF
    if curF%2==0:
        sumOfEven+=curF
    curF,prevF=nextF,curF
print(sumOfEven)
