#STRING SLICING
str1='Bindhu'
print(str1[-1:-7:-1])
  Ans:uhdniB

b = "hello"
print(b[1:3])
  Ans:el

a = 'hello,world'
print(a[2:5])
print(a[:7])
print(a[1:])
print(a[-2:-5])
  Ans:llo
      hello,w
      ello,world

#STRING MODIFICATION
a = 'hello,world'
print(a.upper())
  Ans:HELLO,WORLD

a = 'hello, world '
print(a.strip())
  Ans:hello, world

a = 'hello,world'
print(a.replace('hello','blue'))
  Ans:blue,world

a = 'hello,world'
print(a.split(','))
  Ans:['hello', 'world']

#STRING CONCANATE
str1='my name is jonhn, born in'
str2=' 2000'
txt=str1 + str2
print(txt)
  Ans:my name is jonhn, born in 2000

a = 'hello,world'
print(a.capitalize())
  Ans:Hello,world

#STRING FORMAT
year = 2000
txt = f'my name is john and born in {year}'
print(txt)
  Ans:my name is john and born in 2000

for x in "banana":
    print(x)
    Ans:b
        a
        n
        a
        n
        a

txt = 'i love python'
print('love' not in txt)
  Ans:False

def str_name(s):
    return s[-4:-1]
string='Bindhu'
print('reverse string is:',str_name(string))
  Ans:reverse string is: ndh
