#Write a program that counts the number of vowels in a given string.
  word =input()
count = 0
vow = 'aeiou'
for char in word:
    if char in vow:
        count+=1
print('the no. of vowels:',count)

ANS:
brindha
the no. of vowels: 2
