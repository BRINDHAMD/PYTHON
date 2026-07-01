#Write a program to calculate the sum of the first n natural numbers (where n is input by the user).
  n = int(input('enter a number:'))
sum =0
for i in range(0,n+1):
    sum = sum+i
    print(sum)

ANS:
enter a number: 5
0
1
3
6
10
15

