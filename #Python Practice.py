# in Python instead of using console.log() we use print()
#Can still use single or double quotes 
# Indendtion is REALLY important 

print("Hello World!")

#Variables do not need var, const or let. Just name them and then assign the data 
#rememember to capitalise booleans 

my_name = "Lottie"
my_age = 31
a_member = False
#print(a_member)

#to update a variable you just reassign 

a_member = True
#print(a_member)

#Errors

syntax_error = "an error when you've written something wrong, such as mismatched quotes or a missing bracket"

name_error = "trying to print an undefined variable for example"

#Numbers 

an_int = 2 #a whole num
a_float = 10.5 #a decimal point 

# print(an_int + 3)
# print(a_float / 2)

#performing calculations with python (much like performing calculations with any language )

add = 1+1

minus = 2-1

times = 4*4

division = 70/4

modulo = 90 % 7 

exponentiation = 2**3

#concatenation, joining to variables together 

greeting = "hello"
name = "Yoda"

sign_in_text = greeting + ' ' + name

#print(sign_in_text)

#plus equals, for if you have a variable you need to update eg adding another number 

number_of_miles_hiked = 12

number_of_miles_hiked += 2 

#print(number_of_miles_hiked) - prints out 14

#multi line strings 

this_is_one = """
hello
multiple 
lines """

#control flow - how your programme makes decisions. E.G two cards are played, which one is higher, the higher one wins 

#Boolean - True or False (capitalised in Python)

1 == 1 #equals operator (true)

1 != 2 #not equals operator (this will return true)

1 != 1 #this will return False

'7' == 7 #false cos different data types

a_num = 9

print(type(a_num))

#Function 

def just_a_num(num):
  return num

print(just_a_num(3))

def add_one(num):
  return num + 1


#if Statements - conditional statements IF is raining: bring brolly innit 



#two sums - neetcode video 

def two_sums(nums, target):
  num_result = {}
  