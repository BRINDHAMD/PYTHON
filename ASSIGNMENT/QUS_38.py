#Write a program that implements the FizzBuzz challenge: Print numbers 1 to 50. For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for multiples of both print "FizzBuzz".
for i in range(1,51):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
        continue
    elif i%3==0:
        print('Fizz')
        continue
    elif i%5==0:
        print('Buzz')
        continue
print(i)

ANS:
Fizz
Buzz
Fizz
Fizz
Buzz
Fizz
FizzBuzz
Fizz
Buzz
Fizz
Fizz
Buzz
Fizz
FizzBuzz
Fizz
Buzz
Fizz
Fizz
Buzz
Fizz
FizzBuzz
Fizz
Buzz
