#Maru Puran
#October 12
#Investigating an example of code in order to understand more about functions and subroutines and their differences, as well as the possible ways they can be called

# Example Code

def maths1(): #define maths1
  num1 = 50 #assign number 50 to num1 variable
  num2 = 5 #assign number 5 to num2 variable
  return num1 + num2 #return sum 55

def maths2(): #define maths2
  num1 = 50 #assign number 50 to num1 variable
  num2 = 5 #assign number 5 to num2 variable
  return num1 - num2 #return difference 45

def maths3(num1, num2): #define maths3, allow for arguments to be put inside parameters in num1 and num2
  return num1 * num2 #return product of numbers inserted when subroutine is called

outputNum = maths2() #assign returned value of maths2 subroutine to created variable outputNum, 45
print(outputNum) #prints out 45 the value of outputNum

# How many functions are there in the code?
  # Answer: There is one function in the code.

# How do you know that they are functions, not just subroutines?
  # Answer: Functions are built in, while the subroutines are defined and created.

# Which functions have parameters?  How can you tell?
  # Answer: Subroutine maths3 and function print has a parameter. Inside the parentheses there's a space for the user to enter arguments, for example the values of num1 and num2, when calling the function or subroutine.

# Which functions are called in the code?
  # Answer: Subroutine maths2 and function print are called in the code.

# How do you know which lines of code belong to a function or subroutine?
  # Answer: The lines of code which belong to a function or subroutine are indented beneath their respective functions or subroutines.
