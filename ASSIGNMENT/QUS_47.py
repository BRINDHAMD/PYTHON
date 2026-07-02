#Implement error handling (try/except) to safely handle a ZeroDivisionError when dividing two numbers.
try:
    num_of_items = int(input('how many items'))
    total_price = 200*num_of_items
    avg_price = total_price/num_of_items
    print('avg_price:',avg_price)
except ZeroDivisionError:
    print('you cannot order 0 items')
print('next code block')

ANS:
how many items 0
you cannot order 0 items
next code block
