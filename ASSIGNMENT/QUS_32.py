#Count the occurrences of each character in a string using a dictionary.
word = 'apple'
count = {}
for ch in word:
    if ch in count:
       count[ch] += 1
    else:
        count[ch] = 1
print('the occurence is:', count)

ANS:
the occurence is: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
