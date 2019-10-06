# Find the largest palindrome made from the product of two 3-digit numbers.

# Returns True if reversed string is equal to the string received as parameter
def isPalindrome(string):
    tempList=list(string)
    tempList.reverse()
    if (''.join(tempList)==string):
        return True

# Finds largest palindrome made from the product of numbers in a certain range
def findLargestPalindrome(start, end, step):
    palindrome=0
    for i in range(start,end,step):
        for a in range(start,end,step):
            product=i*a
            if(isPalindrome(str(product))):
                palindrome=max(product,palindrome)
    print(palindrome)

findLargestPalindrome(999,99,-1)
