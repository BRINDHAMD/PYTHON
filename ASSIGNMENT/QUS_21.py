#Define a function is_prime(num) that returns True if a number is prime and False otherwise.
  def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print("False")
                break
        else:
            print("True")
    else:
        print("False")

is_prime(9)

ANS:
False
