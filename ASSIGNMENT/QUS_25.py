#Write a function that calculates the factorial of a number using a loop.
def fact_num(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
result = fact_num(5)
print('the factorial of number is:',result)

ANS:
the factorial of number is: 120
