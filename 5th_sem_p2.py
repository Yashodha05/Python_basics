#To accept input string:  
input_string = "Python is a high-level, general-purpose programming  language."  
print("The input string is:", input_string)  

#To count occurrences of all characters within a string:  
mySet = set(input_string)  

# To create a set of all the characters present in the input for element in mySet: 
for element in myset: 
  countOfChar = 0  
  for character in input_string: 
    if character == element:  
      countOfChar += 1  
  print("Count of character '{}' is {}".format(element, countOfChar))  
