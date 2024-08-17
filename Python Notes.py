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

emptydict={} 
'''
# marks={'Hammy':32, 'James':21, 'list' :[1,2,3], 0:'Person'} #Where Hammy is key and 32 is the value thus Key:value pair
# print(marks['Hammy']) #This will print the marks of Hammy
# print(type(marks)) #Dict = dictionary
# print(marks['list']) #Yes we can also put lists inside a dictionary

"""Dictionary Methods (Important)"""

# dictname={  "name": "Hammy",
#             "from": "Singapore",
#             "marks" : [92] }
 
# print(dictname.items()) # Returns items of dictionary in the form of (key,value) tuples.

# print(dictname.keys()) # Returns keys in the dictionary

# dictname.update({"marks":94}) # Updates the orignal dictionary with supplied key-value pairs. key has to stay same but value can be changed
# dictname.update({"Age":21}) # We can also add key value pairs into the dictionary using the .update() function 
# print(dictname)

# print(dictname.get("name")) # Returns the value of the specified keys (and value is returned eg. "Hammy" is returned here).

# dictname.pop('name') #Pop method removes the given key with its value from the dictionary
# print(dictname)

"""Sets (Important)"""
'''Set is a collection of non-repetetive well defined objects/elements (Yes these are the sets we studied in school)'''

'''
PROPERTIES OF SETS
1. Sets are unordered => Element's order doesn't matter
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values.
'''
'''Syntax 
setvarname={1,2,3}
We use emptyset=set() to make an empty set (read the note underneath this line) 
NOTE:We DONT use setname={} to make an empty set because it creates an empty dictionary instead 
'''

# set1={1,5,2,5,74,2,"Hammy"} #5 and 2 is repeated here but in sets elements cannot be repeated
# print(set1) # Output= {1,2,5,74}



"""Methods of Sets (Important)"""

# set1={1,5,2,74,2,"Hammy"}
# set1.add(230) #This will add the given element into the set
# print(set1)

# set1.remove(1)  # Removes 1 from the set
# print(set1)

# set1.clear() #Removes everything from the set
# print(set1) 

'''Union and intersection in sets(Important)'''

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# # Union (combines all elements) 
# unionset = set1.union(set2)
# print(unionset)  # Output: {1, 2, 3, 4, 5}

# # Intersection (elements common to both sets)
# intersectionset = set1.intersection(set2)
# print(intersectionset)  # Output: {3}

"""Program to let a user print meanings of 3 words using dictionary"""

# list1={'ephemeral':'Lasting for a short time',
#        'serendipity':'The occurrence of events by chance in a happy or beneficial way',
#        'quintessential':'Representing the most perfect or typical example of a quality or class'}

# print(list1.keys())
# chosen=input("Choose which word you want the meaning of:")
# print(list1.get(chosen))

"""Write a program to input 6 numbers from the user and display all the unique
numbers (once) and then print their sum."""

# set1=set() #Empty set
# num=int(input("Enter Number:"))
# set1.add(num)
# num=int(input("Enter Number:"))
# set1.add(num)
# num=int(input("Enter Number:"))
# set1.add(num)
# num=int(input("Enter Number:"))
# set1.add(num)
# num=int(input("Enter Number:"))
# set1.add(num)
# num=int(input("Enter Number:"))
# set1.add(num)
# print(set1)
# print(sum(set1))

"""Program to check if integer and floating number are considered a single element in python"""

# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s)) #output will be 2 This is because python interpreter wil consider 20 and 20.0 as equals thus being a same number there will be no repitition in sed

"""Program to check the type of s={} and how to make a empty set"""

# s={}
# print(type(s))

# set1=set()
# print(type(set1))

"""Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique."""
"""Also check what happens if two of the friends's names are same"""

# dict1={}
# n1=input("Enter your name: ")
# l1=input("Enter your favourite language: ")
# dict1.update({n1:l1})
# n1=input("Enter your name: ")
# l1=input("Enter your favourite language: ")
# dict1.update({n1:l1})
# n1=input("Enter your name: ")
# l1=input("Enter your favourite language: ")
# dict1.update({n1:l1})
# n1=input("Enter your name: ")
# l1=input("Enter your favourite language: ")
# dict1.update({n1:l1}) #if two languages are same then python will keep them seperate because key is what differenciates the pairs
# print(dict1) #If two names are entered same then python will update they key of that friend and use the one who entered the language afterwards

"""Chapter 6, Conditional Expressions"""
'''They allow you to write concise code that performs different actions based on whether a condition is True or False.'''
'''if else elif (else if)'''
"""if the number is divisible by 2 then the number is even, if not (else) it is odd
if n/2:
    print("Number is even") where the tabular space(important) is called Indentation 
else:                       to get out of the body of the conditional statement you remove the indentation
    print("Number is odd")                          
"""

"""Basic program for Age using conditional statements (if elif else ladder)"""
"""In python conditions we use conditional operators and logical operators such as >= <= == etc as discussed before"""

# age=int(input("Enter your age: "))

# if(age>=18): #If age is greater than OR equal to 18
#     print("You are eligible to drive.")
# elif(age<18): #if age is below 18
#     print("You are not eligible to drive.")
# elif(age<0): #if age is below 0 
#     print("Age cannot be negative.")
# else: #This else is only executed if all the other if and elif conditions fail
#     print("You entered an invalid value.") #Checks for error if the value is something other than a number\
#     #Anything written within the indent is included in the block of else statement

# print("End of program.") #Written outside block of else statement

"""Write a program to find the greatest of 3 numbers entered by the user"""

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))

# if(a>=b and a>=c): #Here logical operator and is used which checks if both conditions are true then the whole statement is true
#     print(a,"is the greatest number.")
# elif(b>=a and b>=c): # if b is greater than a and b is greater than c print b is greatest number
#     print(b,"is the greatest number.")
# elif(c>=b and c>=a): #We can also use more than one logical operator inside one conditional statement e.g if(a>b and a>c and a>d):
#     print(c,"is the greatest number.") 
# else:
#     print("Invalid number.")

"""Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user out of total marks 100."""

# marks1=int(input("Enter marks in first subject:"))
# marks2=int(input("Enter marks in second subject:"))
# marks3=int(input("Enter marks in third subject:"))

# totalmarks=marks1+marks2+marks3
# totalpercentage=(100*(totalmarks))/300

# if(totalpercentage>=40 and marks1>33 and marks2>33 and marks3>33):
#     print("You have passed,",totalpercentage)
# else:
#     print("You have failed.", totalpercentage)

"""A spam comment is defined as a text containing following keywords:
"Make a lot of money", "buy now", "subscribe this", "click this". 
Write a program to detect these spams."""

'''In Python the 'in' operator is used to check for membership and containment. it works in:
lists, Tuples, Sets: Check if an element is a member of the collection.
Dictionaries: Check if a key is present in the dictionary.
Strings: Check if a substring is present within the string.
Ranges: Check if a value is within a specified range.'''

# spam1="Make a lot of money"
# spam2="buy now"
# spam3="subscribe this"
# spam4="click this"

# message=input("Enter your comment:")
# if((spam1 in message) or (spam2 in message) or (spam3 in message) or (spam4 in message)): #We will use the find in function to check if the following are IN the message
#     print("This comment is spam.")
# else:
#     print("Your comment was not spam.")

"""Write a program to find whether a given username contains less than 5 characters or not."""

# username=input("Enter your username:")
# lengthofuser=len(username)
# if (lengthofuser<5):
#     print("Your username is smaller than 5 characters.")
# elif (lengthofuser>=5):
#     print("Your username is greater than 5 characters.")

"""Write a program which finds out whether a given name is present in a list or not."""

# namelist=['hammy','joe','chuck']
# checkname=input("Enter a name to check if it is present in the list or not:")
# if (checkname in namelist):
#     print("This name is in the list.",namelist)
# else:
#     print("This name is not in the list.")

"""Write a program to calculate grades of a student."""

# marks = int(input("Enter your marks: "))

# if(marks<=100 and marks>=90):
#     grade = "A+"
# elif(marks<90 and marks>=80):
#     grade = "B"
# elif(marks<80 and marks>=70):
#     grade = "C"
# elif(marks<70 and marks>=60):
#     grade = "D"
# elif(marks<60 and marks>=50):
#     grade = "E"
# elif(marks<50):
#     grade = "F"

# print("Your grade is:", grade)

"""Write a program to find if the name hammy is present in a message or not."""

# message=input("Enter your message: ")
# if("hammy" in message): #in function can check strings, lists, tuples, sets etc 
#     print("Name hammy is present in the message.")
# else:
#     print("Name Hammy is not present in the message.")


"""Chapter 7, Loops in python"""
"""In Python, loops are used to execute a block of code repeatedly. They help automate repetitive tasks and can make your code more efficient and readable.
There are two primary types of loops in Python which are 'for' and 'while' """

'''The for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or other iterable objects.'''

'''Syntax: 
for variable in sequence:
    Code block to execute  '''

'''The while loop repeatedly executes a block of code as long as a specified condition is true.
in while loop we have to somehow make it so the condition thats given becomes false after some time or else the loop will execute infinitly'''

'''Syntax: 
while (condition):
    Code block to execute
'''

'''Write a program to print to print 50 numbers using a while loop'''

# i=1 #Starts i from 1
# while (i<=50): #this will keep checking the condition again and again till its true 
#     print(i) 
#     i=i+1 #This will add 1 each time the loop is executed. it can also be written as i+=1

'''Write a program to print the content of a list using while loop'''

# list1=['hammy','john','joe']
# i=0 #i is zero because index of list starts from 0
# while (i<len(list1)): #This will check the length of the list and since range index is smaller than length of list it will run the code
#     print(list1[i])  
#     i+=1

'''For loop'''
'''#for 'variable' in 'range'/(sequence):'''
'''The range function in Python is used to generate a sequence of numbers, which is commonly used in loops, particularly for loops.
Syntax(start, stop, step size)''' 

# for i in range(0,4):  #this will print i from 0 to range-1 (3) and it will automatically add 1 each time due to the range already being given 
#     print(i) 

# list1=[1,51,12,561,5]
# for num in list1: #Where num is a variable that gets assigned the values from the list and then gets output
#     print(num)

'''For loop can also be used with a else, which is executed when the loop gets exausted'''

# l=[1,5,4,5]
# for i in l:
#     print(i)
# else:
#     print("Loop ended")

'''Break and Continue statements'''

# for i in range (100): #by default range starts from 0 (0,100)
#     if(i == 34): #if the value of i becomes 34 the loop with break
#         break # exits the loop
#     print(i)
    
# for i in range(0,30):
#     if(i==10 or i==20):
#         continue  #This skips the iteration if values are 10 and 20 
#     print(i)

"""Write a program to print the multiplication table of a given number using for loop"""

# num=int(input("Enter the number you want the table for: "))
# till=int(input("Enter the times you want to multiply it: "))
# for i in range(1,till+1):
#     print(num,"x",i,"=",num*i)

"""Write a program to greet all the people whose names stored in a list 'l' and start with S.
list1=["Hammy" "Sammy" "Sunny" "joe"]"""

# list1=["Hammy","Sammy", "Sunny", "joe"]
# for names in list1:
#     if (names[0] == "S"): #Checks if the index 0  of the name is an S 
#         print("Greetings ",names)

"""Write a program to print the multiplication table of a given number using while loop"""

# num=int(input("Enter the number you want the table for: "))
# till=int(input("Enter the times you want to multiply it: "))

# i=1
# while(i<=till): 
#     print(num,"x",i,"=",num*i)
#     i=i+1

"""Write a program to find whether a given number is prime or composite."""

# num=int(input("Enter the number you want to check if its prime or not: "))

# for i in range(2,num): #if divisor is found then number is not prime
#     if num%i==0: 
#         print("Number is composite") 
#         break
# else: 
#     print("Number is prime")

"""Write a program to find the sum of first n natural numbers using while loop."""

# num=int(input("Enter the number: "))
# i=1 #This is for the loop
# sum=0 #sum is initialized with zero and stored in memory
# while(i<=num): #i will go from 1 to n
#     sum=sum+i 
#     i=i+1 #Number is incremented everytime loop re iterates thus increasing it by 1 and adding it to the sum of numbers
# print(sum)

"""Write a program to calculate the factorial of a given number using for loop."""

# num=int(input("Enter the number to calculate its factorial: "))
# fact=1
# for i in range(1,num+1):  #n=1 because range goes till n-1
#     fact=fact*i #value of factorial * i (1,2,3,4,5..) will be assigned to factorial and printed at the end
# print(fact)

"""Write a program to print the following star pattern.
  * 
 **
*****
 """
'''end parameter tells the print function what to print at the end. by default it is \\n new line char'''

# n = int(input("Enter the number: "))
# for i in range (1, n+1) : #range from 1 to (n-1)+1 (3) in this case 
#     print(" "*(n-i), end="") #This will print spaces e.g 3-1 so 2 spaces at first and loops 
#     print("*"*(2*i-1),end="") #This will print the stars in odd number form e.g 2*1-1 = 1,  2*2-1 = 3 and so on
#     print("") #This will add a new line by default because end parameter is not used here


