"""
Problem 2:

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    
    1,2,3,5,8,13,21,34,55,89,...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

# Initializing starting values
a=1
b=2

# Initializing the sum
sum=0

while(b<=4E+6):
    # Finding the next term in the series
    c=a+b

    # Checking if the last term was even
    if(b%2==0):
        sum+=b

    # Updating the previous terms
    a=b
    b=c

print(sum)