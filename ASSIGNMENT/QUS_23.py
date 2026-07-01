#Create a function that accepts a list of numbers and returns their average.
  def avg_num(my_list):
   avg = sum(my_list)/len(my_list)
   return avg
my_list = [1,2,3,4]
result = avg_num(my_list)
print('the average of num is:',result)

ANS:
the average of num is: 2.5
