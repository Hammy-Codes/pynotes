'''Chapter 1, Basic idea of Python and what its like.'''
'''Note: This code was written in Visual Studio, if you use that then you can use the shortcut keys'''
'''Note: You can select a parts of this code(written after #) and un-comment it using CTRL + / to use it'''
'''Note: To execute the code you can just click Ctrl + F5'''
'''Important parts are marked with (Important)'''

# print("Hello")

'''Modules in python are basically pre written codes for us to use by other users'''

"""There are two types of modules in python which include Internal and External modules
External modules need to be installed to be used"""

'''Pip is the package manager for python and that is what we use to install the modules
 Syntax being pip install modulename''' 
# NOTE: This has to be done outside of python interpreter


'''You can import a module in python using import modulename'''
# pip install pyjokes (Outside the interpreter)

# import pyjokes 
# joke=pyjokes.get_joke() # which is a function to assign the joke to the variable joke
# print(joke) #This will print the joke variable in which the joke was stored

'''We can use python as a calculator (Within the interpreter) >>> '''
#print(9+2)
# This will open Repl which is Read Evaluate print loop (This is what python will do)

"""This is a 
Multiline comment, although it isnt used as much as """
# Single line comments because single line comments are easier to toggle by using Ctrl + / key

# print("""we can use 
# triple,single or double quotes to print in multi lines""")

"""Using REPL to print table of 5"""
# We open cmd first and then type python
# Then we just type 5*n and after printing one we can just click on upward arrow key to put the cmd in place of our cursor

"""Installing a module called pyttsx3 which converts text to speech"""
# Go to terminal and type 
# pip install pyttsx3 NOTE: this has to be done outside the python interpreter in the terminal e.g I:\Vs projects>
'''Code'''
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello world, i am a python module.") #This will be the output from your speakers haha
# engine.runAndWait()

'''Program to print the contents of a directory using the os module'''
# import os
# # Select the directory whose content you want to list (by default its inside the folder you are in)
# directory_path = '/'
# # This will assign the path from where you need to search
# contents = os.listdir(directory_path)
# # Checks the directory path and assigns the list (Names) to the variable called contents
# print(contents)


'''Chapter 2, Variables and Data Types in Python'''


"""Variable is basically a container where your values are stored, These can be strings, numbers etc."""
"""Here the strings, numbers etc are different types of values/different data types
Primary data types in python are 

Integers-
Floating point numbers (decimal values)
Strings
Booleans
None

But python is a smart language so it automatically identifies the values for us
Variables can also be called as identifiers (Names)
"""


"""Basic values of different data types being stored in a variables"""
# a=1 #Integer value
# b="Hammy" #String variable
# c=32.42 #this is a floating point number
# d=True # or False with capital T and F are boolean values
# e=None #None meants nothing or empty

"""Very basic calculator"""
# a=1 #1 is stored in the variable "a" where a is name of a memory location
# b=2
# print(a+b)

"""Python Has rules for defining variables"""
'''
These rules are:
A variable name can contain alphabets, digits and underscores
A variable name can only start with an alphabet or an underscore
A variable name cannot start with a number
A variable name cannot contain a white space

'''

"""Operators in python"""
'''
Assignment operators + - * / %   add diff prod div remainder
Arithmatic ops = += -= 
Comparison operators == >= <= != < >  is equal to, less than or equal to, ..., NOT equal to, greater than, less than
The answer/value of comparison operators is always in boolean

Logical operators and or not (Needs To be learned through truth table)

'''

"""Type() Function and Type casting"""
# a = "31.2" #This is initially defined as a string variable due to the double quotes but it can be converted into float if that is valid
# b = float(a) #We can type cast(Change the datatype) using float(), int(), str() etc 

# t = type(b) #The type(x) function shows us the type of the data, This will output as class 'float' e.g
# print(t)

# d= int("32") #This will convert the string into an integer directly
# print(type(d)) #This will print the type

"""Taking numbers from users"""

'''We can relplicate a line with the shortcut Alt Shift Down'''
'''We can select the current line using Ctrl Shift Left'''

'''Fun fact, the default input by python will be in string lol so you have to specify its data type 
which is basically Type Casting the string
e.g a=int(input("enter no."))
'''
# a=int(input("Enter First number: ")) #This will ask the user to enter first number.
# b=int(input("Enter Second number: ")) #This will ask the user to enter second number
# print("Sum of numbers= ", a+b) #This can also be used to concatinate (Join) the two strings "hammy"+"Codes" = Hammy Codes
# print("Difference of numbers= ", a-b)
# print("Product of numbers= ", a*b)
# print("Division of numbers= ", a/b)

"""Program to print the remainder of two numbers"""
'''This basically uses division to print the remainder of the given values'''

# a=int(input("Enter First number: "))
# b=int(input("Enter Second number: "))

# print("Remainder of the two numbers=", a%b ) 

"""Use comparison operator to find out whether a given variable 'a' is greater than 'b' or not. Take a = 34 and b = 80 """
# a=34
# b=80
# print("Is A greater then B?",)
# print("Answer=",a>b)

"""Program to find Average of Two Numbers"""
# a=int(input("Enter First number: "))
# b=int(input("Enter second number: "))
# print("Average of the numbers",a,"and",b,"=",(a+b)/2) #We have to use brackets here because it evaluates division first

"""Program to calculate the Square of a number entered by the user"""
# a=int(input("Enter a number: "))
# print("Square of the number:",a*a)


"""Chapter 3, Strings"""
"""NOTE: Strings are Immutable, which means that they cant be changed, although they can be copied, and the copy of string can be editted basically"""
'''String is a sequanece of characters, it is usually written within quotes'''
'''String index starts from 0 from left to right and -1 from left to right'''

# name="Hammy" #This is a string and H is at 0 Index and y is at -1 Index, the length of this string is 5 and its index is (0,1,2,3,4) LEFT TO RIGHT OR (-5,-4,-3,-2,-1)rIGHT TO LEFT
# print(name)


'''String Slicing'''
'''A string can be sliced to get a part of a string,
Syntax 
strname = "Hammy"
strsliced = strname[0:3] where index is 0 to 3 BUT 0 indexed character is included and 3 index is excluded so its orignal range is 0 to 2 not 0 to 3
strsliced = strname[-3:-1+1] where index is 0 to 3 BUT 0 indexed character is included and 3 index is excluded so its orignal range is 0 to 2 not 0 to 3

''' 

'''We can move whole lines up and down using ALT + UP/DOWN'''

# strname="Hammy"
# strsliced= strname[0:3] # [starting index : Ending index (Excluded)] This is basically the range
# print(strsliced) #This will print the character at 0,1 and 2 because 3 is excluded (Ham)
'''We can also do negative slicing by just converting the corresponding indicies to positive indices
e.g [-4:-1]
can also be written as [1:4]
'''

'''If nothing is written in the range [:] it means [0:Length of string - 1] by default'''

"""String slicing with skip value"""
'''This basically means that it will print the string with the given range of indices and skip the given number of indices'''

# strname= "0123456789"
# strsliced= strname[0:8:2] #prints index values from 0 to 7 (8 is excluded) and jumps by 2 everytime
# print(strsliced) 

"""String Functions"""

'''String length len(str)'''

# name = "Hammy"
# print(len(name))

'''String ends with name.endswith(" ")'''

# name="Hammy"
# print(name.endswith("mmy")) #Checks if the name ends with mmy (True in this case)

'''String Starts with name.startswith(" ")'''

# name="Hammy"
# print(name.startswith("Ham")) #Checks if the name Starts with HAM (True in this case) (Case sensitive)

'''String capitalize (First letter only)'''

# name="hammy"
# print(name.capitalize())

'''string.count(" ") counts the number of times a character has occured'''

# s = "hello mello"
# print(s.count("e"))  # Output: "2"

'''Find function string.find("word")''' #This function friends a word and returns the index of first occurrence of that word in the string.

# strname = "hello world"
# index = strname.find ("world")
# print(index) # Output: 6

'''strname.replace(" initial ", " new ") replaces all occurences of a certain word in a string'''

# strname= "Hammy is a Good boy"
# print(strname.replace("Good","Bad"))

'''There are way to many to cover here so you can Use chat gpt to see all the string functions'''
# str = "Hello World"
# print(str.lower())  # Output: "hello world"

# str = "Hello World"
# print(str.upper())  # Output: "HELLO WORLD"

# str = "hello world"
# print(str.title())  # Output: "Hello World"


"""Escape sequences in python  (More than one characters in writing but represent one character)
They have to be used with BACKSLASH \\ (Above enter key)"""

'''Some escape sequences are 
\t Skips by 8 spaces gap
\n Moves the rest of string in a new line
\' or \"  Quotes inside a string e.g " Hello \"World\" "
\\ Backslash 
\a beep sound
There are more so you can Check Escape sequence in python using chat gpt
'''

"""Program to display a user entered name followed by Good
Afternoon using input function"""

# string=input("Enter Your Name: ")
# print("Good Afternoon",string)

"""Program to replace Name with Name and date with date"""

# letter = '''Dear <|Name|>, 
# You are selected! 
# <|Date|> '''

# print(letter.replace("<|Name|>","Hammy").replace("<|Date|>","1st September 2024"))

"""Write a program to detect double space in a string."""

# string="Hey my name is  Hammy"
# print("Double space detected at Index",string.find("  ")) #The output is -1 if it cant find the given characters

"""Replace the Double space with single space in the above problem"""

# string="Hey my name is  Hammy"
# print(string.replace("  "," "))


"""Chapter 4, Lists and Tuples"""

"""Lists, Lists are often used when you need a collection of items that may need to change during the program's execution."""
"""Python lists are containers to store a SET of values of ANY datatype"""

# friends=["Apple",False,32.4,"Hammy"]
# print(friends[0])

# '''Unlike strings(Immutable), we can change the items of a list (Mutable)'''

# friends[0]="Bottom Jeans" #Here the string Apple was changed to Bottom jeans 
# print(friends[0])

# '''Like strings we can also do slicing of lists'''

# print(friends[0:2]) #Where two is ignored


"""LIST METHODS. (important)"""

# L1 = [1,8,7, 2, 21, 15]
# L1.sort() # sorts the list
# print(L1)
# L1.reverse() # reverse sorts the list in decending order
# print(L1)
# L1.append(8) #adds 8 at the end of the list
# print(L1)
# L1.insert(3,33333) #This will add 33333 at 3rd index which is 4rth place List.insert(index,)
# print(L1)
# L1.pop(2) #Will delete element at index 2 and retum the list without the element
# print(L1)
# L1.remove(21) #Will remove 21 from the list
# print(L1)

"""Tuples, They are often used to represent fixed collections of items, such as coordinates or records where you want to ensure the data remains unchanged."""
'''Basic syntax of tuples
varname=(number,) we cannot use a number alone because python will then think that its a integer
tup=(12,False,34.5)
Tuples can also have different types of values stored in them at the same time
NOTE:Main thing that differentiates tuple from lists is that the elements of tuple CANNOT be changed (Immutable)
which means that we cannot add,swap or remove anything from it
'''

# varname=(1,2,3,4,1)
# print(varname)
# print(type(varname))

'''Tuple Methods'''

# varname=(12,False,"Hammy",2.3,False)
# counter=varname.count(False) #This will count the times that the Boolean value Has occured 2 Times
# print(counter) #Output = 2

# index=varname.index(2.3) #This will tell us the index of the value
# print(index) #Output = 3


# my_tuple = (1, 2, 3, 4)
# print(my_tuple[1:3])  # Slicing: Extract a portion of the tuple

# # Concatenation: Combine two tuples
# tuple1 = (1, 2)
# tuple2 = (3, 4)
# combined_tuple = tuple1 + tuple2
# print(combined_tuple)  # Output: (1, 2, 3, 4)

# # Repetition: Repeat the tuple
# repeated_tuple = tuple1 * 3
# print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

# # Membership Testing: Check if an element is in the tuple
# print(3 in combined_tuple)  # Output: True Because it Checks if the number 3 is in the tuple 
# print(5 in combined_tuple)  # Output: False

# # Length: Get the number of elements in the tuple
# print(len(my_tuple))  # Output: 4

"""Write a program to store 3 fruits in a list entered by the user."""

# list1=[] #First we make an empty list
# l1=input("Enter Fruit 1: ")
# list1.append(l1)
# l2=input("Enter Fruit 2: ")
# list1.append(l2)
# l3=input("Enter Fruit 3: ")
# list1.append(l3)

# print(list1)

"""Write a program to take marks of 3 students and sort them"""
'''We can also make a program similar to this that can sort names of students alphabetically (Just delete the int() part)'''

# marks=[]
# m1=int(input("Enter Marks of student 1: "))
# marks.append(m1)
# m2=int(input("Enter Marks of student 2: "))
# marks.append(m2)
# m3=int(input("Enter Marks of student 3: "))
# marks.append(m3)
# print("Unsorted Marks=",marks)
# marks.sort()
# print("Sorted Marks=",marks) 
'''You should Also submit your code to chatgpt and ask him what i can do better here or what i did wrong'''

"""Write a program that finds Sum of 4 numbers USING LISTS"""

# sumvar=[1,5,7,9]
# print("Sum of the list",sum(sumvar)) #Yes its that easy, you can just use the sum function to find the sum of the elements of the list

"""Write a program to find the number of zeros in a tuple"""

# tuple1=(0,1,5,0,2,0,33,0)
# print("Amount of times Zero occured in given tuple=",tuple1.count(0)) #Output = 4

"""Chapter 5, Dictionary and Sets (Important)"""
'''Dictionary is a built-in DATA TYPE that stores key-value pairs. 
Each key is unique and maps to a value, allowing for fast retrieval, addition, and modification of data.
Lists are unordered, mutable and indexed and they cannot contain duplicate keys
'''
'''Syntax
dictionaryname={'name':'Hammy', 'Age':32}
'''
# marks={'Hammy':32, 'James':21, 'list' :[1,2,3], 0:'Person'} #Where Hammy is key and 32 is the value thus Key:value pair
# print(marks['Hammy']) #This will print the marks of Hammy
# print(type(marks)) #Dict = dictionary
# print(marks['list']) #Yes we can also put lists inside a dictionary

"""Dictionary Methods (Important)"""
dictname={  "name": "Hammy",
            "from": "Singapore",
            "marks" : [92] }
 
print(dictname.items()) # Returns items of dictionary in the form of (key,value) tuples.

print(dictname.keys()) # Returns keys in the dictionary

dictname.update({"marks":94}) # Updates the orignal dictionary with supplied key-value pairs. key has to stay same but value can be changed
print(dictname)

print(dictname.get("name")) # Returns the value of the specified keys (and value is returned eg. "Hammy" is returned here).

