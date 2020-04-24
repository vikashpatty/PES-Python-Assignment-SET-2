#!/usr/bin/env python
# coding: utf-8

# 21.Using the built-in functions on Numbers perform following operations
# 
# a) Round of the given floating point number. Example:  n=0.543 then round it next decimal number, i.e n=1.0 Use round() function
# 
# b) Find out the square root of a given number. (Use sqrt(x) function)
# 
# c) Generate random number between 0, and 1 ( use  random() function)
# 
# d) Generate random number between 10 and  500. (Use uniform() function)
# 
# e) Explore all Math and Random module functions  on a given number/ List.
# 

# In[4]:


import math
import random

n=0.543
print("round number for the entered number: ",round(n))
print("square root of the number is: ",math.sqrt(n))
print("random number from 0 to 1= ",random.random())
print("random number from 10 to 500: ",random.uniform(10,500))

print(math.pi)
print(math.e)
print(math.radians(n))
print(math.sin(n))
print(math.cos(n))
print(math.tan(n))
print(math.log(n))
print(math.pow(2,3))
print(math.ceil(n))

print(random.shuffle([1,2,3,4]))
print(random.randint(1,100))
print(random.choice([5,6,7,8]))


# 22.Read the value x and y from the user and apply all trigonometric functions on these numbers. 
# 
# Note: Refer the tutorial Trigonometric operation table

# In[6]:


import math

x=eval(input("write x value:"))
y=eval(input("write y value:"))

print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print(math.asin(x))
print(math.acos(x))
print(math.atan(x))
print(math.atan2(y,x))
print(math.hypot(x,y))


# 23.Find the area of Circle given that radius of a circle. 
# 
# (Use pi value from Math module as mathematical constant)

# In[7]:


import math
r = eval(input("Enter the radius:"))
area=math.pi*r*r
print("Area of the circel is:",area)


# 24.Write program to explore all Escape characters specified in Tutorial (Under String chapter)

# In[10]:


print("\\")
print("\'")
print("\"")
print('ASCII bell makes ringing the bell alert sounds \a')
print('ASCII backspace ( BS ) removes previous character:'+"ab" + "\b" + "c")
print('ASCII formfeed ( FF )'+"hello\fworld")
print('ASCII linefeed ( LF )'+"hello\nworld")
print('Prints a character from the Unicode database'+u"\N{DAGGER}")
print("123456\rXX_XX")
print('ASCII horizontal tab (TAB)'+"\t* hello")
print('Prints 16-bit hex value Unicode character'+u"\u041b")
print('Prints 32-bit hex value Unicode character'+u"\U000001a9")
print('Prints character based on its octal value' + "\043")
print('Prints character based on its hex value'+"\x23")


# 25.Write a program to print the different data types (Numbers, strings characters) using the Format symbols (Refer to different format symbols specified in Tutorial)

# In[13]:


a=1
b="Vikash Pateshwari"
c=1.00
d=[1,2,3,4]
e=(5,6,7,8)
f={1:2,2:3,3:4}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


# 26.Receive the encoded string from your friend & decode it to check the original message. PS: You will receive Encoded string and the Algorithm used for encoding.

# In[16]:


x=str(input('Enter the msg to encode:'))

print(x.encode(encoding="ascii",errors="backslashreplace"))
print(x.encode(encoding="ascii",errors="ignore"))
print(x.encode(encoding="ascii",errors="namereplace"))
print(x.encode(encoding="ascii",errors="replace"))
print(x.encode(encoding="ascii",errors="xmlcharrefreplace"))
print(x.encode(encoding="ascii",errors="strict"))


# 27.Write a program to check given string is Palindrome or not.That is reverse the given string and check whether it is same as original string, if so then it is palindrome.
# 
# Example: String = "malayalam"  reverse string = "malayalam" hence given string is palindrome. Use built functions to check given string is palindrome or not.
# 

# In[20]:


x=str(input('Check the string if palindrome or not:'))
if x==x[::-1]:
    print('The Given string {} is palindrome'.format(x))
else:
    print('Non Palindrome String')


# 28.Write a program to check how many ovals present in the given string. That is, count the number of " a e i o u" in the given string and print the numbers against each oval. 
# 
# Example:- "This is Python" Number of total ovals = 3, i = 2, o =1

# In[24]:


def Check(x, vowels): 
    final = [i for i in x if i in vowels] 
    print(len(final)) 
    print(final) 
       
x=str(input('Enter the string to check vowel count:')).lower()
vowels = "aeiou"
Check(x, vowels);


# 29.Apply all built in functions on Strings in your program. Note: There are 40 string functions. Use Tutorial for the help.
# 
# Note: Each program should have 5 string built in functions(so write 8 programs to cover all string functions)

# In[35]:


x=str(input("Enter The string to perform 1st five builtin function:"))
#give input This is 1st string

#Return a capitalized version of the string.
#More specifically, make the first character have upper case and the rest lower case.
print(x.capitalize())

#Return a version of the string suitable for caseless comparisons.
print(x.casefold())

#Return a centered string of length width.
#Padding is done using the specified fill character (default is a space).
print(x.center(10,'z'))

#Return the number of non-overlapping occurrences of substring sub in
#string S[start:end].  Optional arguments start and end are
#interpreted as in slice notation.
sub='i'
print(x.count(sub,1,10))

sub='lol'
print(x.count(sub))

#encode(self, /, encoding='utf-8', errors='strict')
#Encode the string using the codec registered for encoding.
#The encoding in which to encode the string.
#errors
#The error handling scheme to use for encoding errors.
#The default is 'strict' meaning that encoding errors raise a
#UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
#'xmlcharrefreplace' as well as any other name registered with
#codecs.register_error that can handle UnicodeEncodeErrors.
print(x.encode('utf-8','strict'))

0

y=str(input("Enter string to perform next 5 function:"))
#give input this is 2nd string

z='ing'

#Return True if S ends with the specified suffix, False otherwise.
#With optional start, test S beginning at that position.
#With optional end, stop comparing S at that position.
#suffix can also be a tuple of strings to try.

print(y.endswith(z))
print(y.endswith(z,10))
z='s'
print(y.endswith(z, 1, 4))
print(y.endswith(z, 2, 6))

#Return a copy where all tab characters are expanded using spaces.
#If tabsize is not given, a tab size of 8 characters is assumed.

print("\noriginal string:",y)
print(y.expandtabs())
print(y.expandtabs(16))

#Return the lowest index in S where substring sub is found,
# that sub is contained within S[start:end].  Optional
#arguments start and end are interpreted as in slice notation.
#Return -1 on failure.

k='tr'
print(y.find(k))
print(y.find(k, 10))
print(y.find(k, 40))

#Return a formatted version of S, using substitutions from args and kwargs.
#The substitutions are identified by braces ('{' and '}').

l="Hi i'm {age:.2f} year old!"
print(l.format(age = 200))

#Return a formatted version of S, using substitutions from mapping.
#The substitutions are identified by braces ('{' and '}').
#print(l.format_map())

#Return the lowest index in S where substring sub is found, 
#such that sub is contained within S[start:end].  Optional
#arguments start and end are interpreted as in slice notation.
#Raises ValueError when the substring is not found.
print(l.index("old"))
 
#Return True if the string is an alpha-numeric string, False otherwise.
#string is alpha-numeric if all characters in the string are alpha-numeric and
#there is at least one character in the string.
print(y.isalnum())

#Return True if the string is an alphabetic string, False otherwise.
#A string is alphabetic if all characters in the string are alphabetic and there
#is at least one character in the string.
print(y.isalpha()) 



#Return True if all characters in the string are ASCII, False otherwise.
#ASCII characters have code points in the range U+0000-U+007F.
#Empty string is ASCII too.
print(y.isascii())


#Return True if the string is a decimal string, False otherwise.
#A string is a decimal string if all characters in the string are decimal and
#there is at least one character in the string.
print(y.isdecimal())

#Return True if the string is a digit string, False otherwise.
#A string is a digit string if all characters in the string are digits and there
#is at least one character in the string.
print(y.isdigit())

#Return True if the string is a valid Python identifier, False otherwise.
#Use keyword.iskeyword() to test for reserved identifiers such as "def" and
#"class".
print(y.isidentifier())
    

#Return True if the string is a lowercase string, False otherwise.
#A string is lowercase if all cased characters in the string are lowercase and
#there is at least one cased character in the string.    
print(y.islower())    
    

#Return True if the string is a numeric string, False otherwise.
#A string is numeric if all characters in the string are numeric and there is at
#least one character in the string.
print(y.isnumeric())

#Return True if the string is printable, False otherwise.
#A string is printable if all of its characters are considered printable in
#repr() or if it is empty.
print(y.isprintable()) 
 
#Return True if the string is a whitespace string, False otherwise.
#A string is whitespace if all characters in the string are whitespace and there
#is at least one character in the string.
print(y.isspace())    
    
#Return True if the string is a title-cased string, False otherwise.
#In a title-cased string, upper- and title-case characters may only
#follow uncased characters and lowercase characters only cased ones.
print(y.istitle())    
    
    
#Return True if the string is an uppercase string, False otherwise.
#A string is uppercase if all cased characters in the string are uppercase and
#there is at least one cased character in the string.    
print(y.isupper())


#Concatenate any number of strings.
#The string whose method is called is inserted in between each given string.
#The result is returned as a new string.
j='  Wipro Sarjapur  '
print("#".join(j)) 

#Return a left-justified string of length width.
#Padding is done using the specified fill character (default is a space).
print(j.ljust(20))

#Return a copy of the string converted to lowercase.
print(j.lower())

#Return a copy of the string with leading whitespace removed.
#If chars is given and not None, remove characters in chars instead.
print(j.lstrip())

#Partition the string into three parts using the given separator.
#
#This will search for the separator in the string.  If the separator is found,
#returns a 3-tuple containing the part before the separator, the separator
#itself, and the part after it.
#
#If the separator is not found, returns a 3-tuple containing the original string
#and two empty strings.
print(j.partition(" "))
  
#replace(self, old, new, count=-1, /)
#Return a copy with all occurrences of substring old replaced by new.
#
#  count
#    Maximum number of occurrences to replace.
#    -1 (the default value) means replace all occurrences.
#
#If the optional argument count is given, only the first count occurrences are
#replaced.
print(j.replace("a","b"))
    
    
#rfind(...)
#S.rfind(sub[, start[, end]]) -> int
#
#Return the highest index in S where substring sub is found,
#such that sub is contained within S[start:end].  Optional
#arguments start and end are interpreted as in slice notation.
#
#Return -1 on failure.
print(j.rfind('Wipro'))


#rindex(...)
#S.rindex(sub[, start[, end]]) -> int
#
#Return the highest index in S where substring sub is found,
#such that sub is contained within S[start:end].  Optional
#arguments start and end are interpreted as in slice notation.
#
#Raises ValueError when the substring is not found.
print(j.rindex('Wipro'))


#rjust(self, width, fillchar=' ', /)
#Return a right-justified string of length width.
#
#Padding is done using the specified fill character (default is a space).
print(j.rjust(20))


#rpartition(self, sep, /)
#Partition the string into three parts using the given separator.
#
#This will search for the separator in the string, starting at the end. If
#the separator is found, returns a 3-tuple containing the part before the
#separator, the separator itself, and the part after it.
#
#If the separator is not found, returns a 3-tuple containing two empty strings
#and the original string.
#print(j.rpartinion("a"))



#rsplit(self, /, sep=None, maxsplit=-1)
#Return a list of the words in the string, using sep as the delimiter string.
#
#  sep
#    The delimiter according which to split the string.
#    None (the default value) means split according to any whitespace,
#    and discard empty strings from the result.
#  maxsplit
#    Maximum number of splits to do.
#    -1 (the default value) means no limit.
#
#Splits are done starting at the end of the string and working to the front.
print(j.rsplit(' '))


#rstrip(self, chars=None, /)
#Return a copy of the string with trailing whitespace removed.
#
#If chars is given and not None, remove characters in chars instead.
print(j.rstrip())

#split(self, /, sep=None, maxsplit=-1)
#Return a list of the words in the string, using sep as the delimiter string.
#  sep
#  The delimiter according which to split the string.
#  None (the default value) means split according to any whitespace,
#  and discard empty strings from the result.
#  maxsplit
#  Maximum number of splits to do.
#  -1 (the default value) means no limit.
print(j.split(' '))

#splitlines(self, /, keepends=False)
#Return a list of the lines in the string, breaking at line boundaries.
#
#Line breaks are not included in the resulting list unless keepends is given and
#true.
#print(j.splitlines(' '))


#startswith(...)
#S.startswith(prefix[, start[, end]]) -> bool
#
#Return True if S starts with the specified prefix, False otherwise.
#With optional start, test S beginning at that position.
#With optional end, stop comparing S at that position.
#prefix can also be a tuple of strings to try.
print(j.startswith('Sarjapur'))


#strip(self, chars=None, /)
#Return a copy of the string with leading and trailing whitespace remove.
#
#If chars is given and not None, remove characters in chars instead.
print(j.strip())

#swapcase(self, /)
#Convert uppercase characters to lowercase and lowercase characters to uppercase.
print(j.swapcase())

#title(self, /)
#Return a version of the string where each word is titlecased.
#
#More specifically, words start with uppercased characters and all remaining
#cased characters have lower case.
print(j.title())


#translate(self, table, /)
#    Replace each character in the string using the given translation table.
#    
#      table
#        Translation table, which must be a mapping of Unicode ordinals to
#        Unicode ordinals, strings, or None.
#    
#    The table must implement lookup/indexing via __getitem__, for instance a
#    dictionary or list.  If this operation raises LookupError, the character is
#    left untouched.  Characters mapped to None are deleted.
#print(j.translate())

#upper(self, /)
#    Return a copy of the string converted to uppercase.
print(j.upper())


#zfill(self, width, /)
#    Pad a numeric string with zeros on the left, to fill a field of the given width.
#    
#    The string is never truncated.
#print(j.zfill())


# 30.Write a program to Sort given N numbers (Use only loop structures and Conditions to sort the elements.
# 
# Use Bubble sort / Selection sort technique to sort the elements of List) 
# 
# Note: Don't use built in functions to sort.

# In[43]:


def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1):  
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = [9,1,3,6,77,8]
bubbleSort(arr)
print(arr)


# 31.Write a program to search an element in the list. i.e. Perform the binary search on the sorted list having integers as elements. If the search is successful print "Success" else print "un successful search".

# In[8]:


def binary_search(list_1,x):
    
    findex = 0
    lindex = len(list_1)-1
    f = 0
    while( findex<=lindex and not f):
        mid = (findex + lindex)//2
        if list_1[mid] == x :
            f = 1
        else:
            if x < list_1[mid]:
                lindex = mid - 1
            else:
                findex = mid + 1
    return f

list1=[1,2,3,4,5,6,]
print(list1)
x=int(input('enter the item to find in list:'))

found= binary_search(list1,x)

if found==1:
    print("Success")
else:
    print("un successful search")    


# 32.Write a program to perform following operations on List. Create three lists as List1, List2 and List3 having 5 city names each list.
# 
# a. Find the length city of each list element and print city and length
# 
# b. Find the maximum and minimum string length element of each list
# 
# c. Compare each list and determine which city is biggest & smallest with length.
# 
# d. Delete first and last element of each list and print list contents.
# 

# In[32]:


list1=['gaya','manpur','patwatoli','buniyadganj','bihar']
list2=['delhi','bangalore','mumbai','chennai','kolkata']
list3=['goa','utrakhand','ladhak','kodaikanal','shimla']
for i in list1:
    print("List1 City= {}, lenght={}".format(i,len(i)))
print('-'*50)
for i in list2:
    print("List2 City= {}, lenght={}".format(i,len(i)))
print('-'*50)
for i in list3:
    print("List3 City= {}, lenght={}".format(i,len(i)))

print('-'*50)
print("Max in all the list1: "+max(list1,key = len))
print("Max in all the list2: "+max(list2,key = len))
print("Max in all the list3: "+max(list3,key = len))

print('-'*50)

print("Min in all the list1: "+min(list1,key = len))
print("Min in all the list2: "+min(list2,key = len))
print("Min in all the list3: "+min(list3,key = len))
print('-'*50)

list4=list1+list2+list3
print("Max in all the list: "+max(list4,key = len))
print("Min in all the list: "+min(list4,key = len))

print('-'*50)

del list1[0]
del list1[-1]
del list2[0]
del list2[-1]
del list3[0]
del list3[-1]

print(list1)
print(list2)
print(list3)


# 33.Create a list with 7 elements and perform following operations. Let the list be initialized with List1 any 5 city names;
# 
# a) Append a new city name to the List
# 
# b) Insert a city name at 4th index position
# 
# c) Sort the list and print all elements
# 
# d) Sort the elements of the list in descending order.
# 
# e) delete last three elements using pop operation
# 

# In[58]:


listq=["elemen1","elemen2","elemen3","elemen4","elemen5","elemen6","elemen7"]

print(listq)
listq.append("elemet8")
print(listq)

listq.insert(4,'element9')
print(listq)

listq.sort()
print(listq)

listq.sort(reverse=True)
print(listq)

listq.pop(-1)
listq.pop(-2)
listq.pop(-3)
print (listq)


# 34.Create 3 Lists (list1, list2, list3) with integer and perform following operations
# 
# a) Create Maxlist by taking 2 maximum elements from each list.
# 
# b) Find average value from all the elements of Maxlist.
# 
# c) Create a MinlIst by taking 2 minimum elements from each list 
# 
# d) Find the average value from all the elements of Minlist
# 

# In[69]:


list1=[1,2,3,4,5,6]
list2=[7,8,9,11,10]
list3=[12,1,21,33,23]

list1.sort()
print(list1[-2:])
list2.sort()
print(list2[-2:])
list3.sort()
print(list3[-2:])

list4=list1+list2+list3
def Avg(input):
    avg=sum(input)/len(input)
    return avg

print(Avg(list4))


list1.sort()
print(list1[:2])
list2.sort()
print(list2[:2])
list3.sort()
print(list3[:2])

list4=[]
for i in list1[:2]:
    list4.append(i)
for i in list2[:2]:
    list4.append(i)
for i in list3[:2]:
    list4.append(i)

print(list4)

print(sum(list4)/len(list4))
    


# 35.Create Tuple as specified below;
# 
# a) Create a Tuple tup1 with days in a week & print the tuple elements
# 
# b) Create a Tuple tup2  with months in a year and concatenate it with tup1
# 
# c) Create 3 tuples( tup1,tup2,tup3) with numbers and determine which is greater.
# 
# d) Try to delete an individual element in tup1 and try deleting complete Tuple -tup1 notice the error type you get.
# 
# e) Insert new element in to tuple by typecasting it to List
# 

# In[95]:


tup1 = 'sunday','monday','tuesday','wednesday','thrusday','friday','saturday'
print(tup1)

tup2= 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
print(tup2)

tupcon=tup1+tup2
print(tupcon)

tup1=1,2,3,4,5,6,7
tup2=32,23,34,54,44
tup3=54,54,66,78,99

print(max(tup1))
print(max(tup2))
print(max(tup3))

if len(tup1)>len(tup2) and len(tup1)>len(tup3):
    print('gretest is tup1')
elif len(tup2)>len(tup1) and len(tup2)>len(tup3):
    print('greates is tup2')
else:
    print('greates is tup3')
    
#del tup1[0]
#TypeError                                 Traceback (most recent call last)
#<ipython-input-84-3077302f29b1> in <module>
#     23     print('greates is tup3')
#     24 
#---> 25 del tup1[0]
#
#TypeError: 'tuple' object doesn't support item deletion

#list1=list(tup3)
#list1.append('inseted')
#print(list1)
#
#---> 34 list1=list(tup3)
#     35 list1.append('inseted')
#     36 print(list1)
#
#TypeError: 'list' object is not callable


# 36.Create two tuples tup1 & tup2 and apply all built in functions on tuples. 
# 
# ( Refer Tutorial for the Built in functions list)

# In[97]:


tup1=1,2,3,4,5,6,7
tup2=32,23,34,54,44

print(len(tup1))
print(tup1[1:4])
print(tup1[-1])
print(max(tup1))
print(min(tup1))


# 37.Create 3 dictionaries (dict1, dict2, dict3) with 3 elements each. Perform following operations
# 
# a) Compare dictionaries to determine the biggest.
# 
# b) Add new elements in to the dictionaries dict1, dict2
# 
# c) print the length of dict1, dict2, dict3.
# 
# d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.
# 

# In[103]:


dict1={'hi':1,'bye':2,'hello':3}
dict2={'ram':30,'vikash':24,'sahil':45}
dict3={'gaya':'bihar','howrah':'kolkata'}

if dict1.items()>dict2.items() and dict1.items()>dict3.items() :
    print("dict1 is bigger")
elif dict2.items()>dict3.items() and dict2.items()>dict3.items():
    print("dict2 is bigger")
else:
    print("dict3 is bigger")
    
dict1['adding']=99999
dict2['wipro']='added'
print(dict1)
print(dict2)


print(str(dict1)+str(dict2)+str(dict3))


# 38.Create 2 dictionaries as follows;
# 
# dict1 ={'Name':'Ramakrishna','Age':25}
# 
# dict2={'EmpId':1234,'Salary':5000}
# 
# Perform following operations  
# 
# a) Create single dictionary by merging dict1 and dict2
# 
# b) Update the salary to 10%
# 
# c) Update the age to 26
# 
# d) Insert the new element with key "grade" and assign value as "B1"
# 
# e) Extract and print all values and keys separately.
# 
# f) delete the element with key 'Age' and print dictionary elements.
# 

# In[105]:


dict1 ={'Name':'Ramakrishna','Age':25}

dict2={'EmpId':1234,'Salary':5000}

dict1.update(dict2)

dict1['Salary']=int(dict1['Salary'])*0.1+int(dict1['Salary'])
dict1['Age']=26
dict1['grade']='B1'

print(dict1.keys())
print(dict1.values())

del dict1['Age']
print(dict1)


# 39.Using Time and Calendar module, Print current date and time. Print current month calendar.

# In[117]:


import datetime
today = datetime.datetime.today()

print(today)

print('-'*50)
import calendar
cal = calendar.month(today.year,today.month)

print(cal)


# 40.Using time module perform following operations.
# 
# a) Print current time for every 5 seconds up to 1 minute time interval.
# 
# b) Write a program to find out how much CPU time is taken for the execution of above(32.a)  program.
# 

# In[8]:


import time
from datetime import datetime
i=0
while i<=60:
    print(datetime.now())
    time.sleep(5)
    i+=5


# In[10]:


import timeit    

testcode='''
list1=['gaya','manpur','patwatoli','buniyadganj','bihar']
list2=['delhi','bangalore','mumbai','chennai','kolkata']
list3=['goa','utrakhand','ladhak','kodaikanal','shimla']
for i in list1:
    print("List1 City= {}, lenght={}".format(i,len(i)))
print('-'*50)
for i in list2:
    print("List2 City= {}, lenght={}".format(i,len(i)))
print('-'*50)
for i in list3:
    print("List3 City= {}, lenght={}".format(i,len(i)))
'''

elapsed_time = timeit.timeit(testcode,number=10)
print(elapsed_time)


# In[ ]:




