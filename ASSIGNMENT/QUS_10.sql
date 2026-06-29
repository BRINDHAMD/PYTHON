#Write a simple grading program: A (90+), B (80–89), C (70–79), D (60–69), F (below 60).
  grade = int(input('enter your grade:'))
if grade >= 90:
    print('A')
elif grade >= 80 and grade <= 89:
     print('B')
elif grade >= 70 and grade <= 79:
    print('C')
elif grade >= 60 and grade <= 69:
   print('D')
else:
    print('F')

ANS:enter your grade: 22
F
