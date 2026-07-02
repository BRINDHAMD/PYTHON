#Find the second largest number in a list without sorting the entire list.
my_list = [11, 94, 98, 58]

largest = max(my_list)
second = 0

for n in my_list:
    if n != largest and n > second:
        second = n

print("Second largest number is:", second)

ANS:
Second largest number is: 94
