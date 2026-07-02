#Create a tuple with 5 elements. Try to change one element and observe the error. Write code to convert it to a list, change the element, and convert it back to a tuple.
num = (1,2,3,4)
n = list(num)
n.append(5)
num = tuple(n)
print(num)

ANS:
(1, 2, 3, 4, 5)
