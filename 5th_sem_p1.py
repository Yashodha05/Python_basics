#1.a)Develop a program that accept the list and iterates over a list of numbers first and prints the numbers in the list whose square is divisible by 8. 

num_list = [2, 3, 5, 7, 8, 9, 12, 16]  
for num in num_list:  
  if (num * num) % 8 == 0:  
  print(num) 
