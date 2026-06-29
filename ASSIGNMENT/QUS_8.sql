#Write a program to find the largest of three numbers entered by the user.
  num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 >= num2 and num1 >= num3:
    print('the greatest num is:',num1)
elif num2 >= num3:
   print('the greatest num is:',num2)
else:
   print('the greatest num is:',num3)

ANS: 50
 70
 80
the greatest num is: 80
