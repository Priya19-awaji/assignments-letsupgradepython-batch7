#!/usr/bin/env python
# coding: utf-8

# In[ ]:


String and it's default functions
The functions str.upper() and str.lower() will return a string with all the letters of an original string converted to upper- or lower-case letters. Because strings are immutable data types, the returned string will be a new string. Any characters in the string that are not letters will not be changed.

Let’s convert the string Sammy Shark to be all upper case:

ss = "Sammy Shark"
print(ss.upper())
Ouput
SAMMY SHARK
Now, let’s convert the string to be all lower case:

print(ss.lower())
Ouput
sammy shark
The str.upper() and str.lower() functions make it easier to evaluate and compare strings by making case consistent throughout. That way if a user writes their name all lower case, we can still determine whether their name is in our database by checking it against an all upper-case version, for example.
The string function len() returns the number of characters in a string. This method is useful for when you need to enforce minimum or maximum password lengths, for example, or to truncate larger strings to be within certain limits for use as abbreviations.

To demonstrate this method, we’ll find the length of a sentence-long string:

open_source = "Sammy contributes to open source."
print(len(open_source))
Output
33
We set the variable open_source equal to the string "Sammy contributes to open source." and then we passed that variable to the len() function with len(open_source). We then passed the method into the print() method so that we could see the output on the screen from our program.

Keep in mind that any character bound by single or double quotation marks — including letters, numbers, whitespace characters, and symbols — will be counted by the len() function.

join(), split(), and replace() Methods
The str.join(), str.split(), and str.replace() methods are a few additional ways to manipulate strings in Python.

The str.join() method will concatenate two strings, but in a way that passes one string through another.

Let’s create a string:

balloon = "Sammy has a balloon."
Now, let’s use the str.join() method to add whitespace to that string, which we can do like so:

" ".join(balloon)
If we print this out:

print(" ".join(balloon))
We will see that in the new string that is returned there is added space throughout the first string:

Ouput
S a m m y   h a s   a   b a l l o o n .
We can also use the str.join() method to return a string that is a reversal from the original string:

print("".join(reversed(balloon)))
Ouput
.noollab a sah ymmaS
We did not want to add any part of another string to the first string, so we kept the quotation marks touching with no space in between.

The str.join() method is also useful to combine a list of strings into a new single string.

Let’s create a comma-separated string from a list of strings:

print(",".join(["sharks", "crustaceans", "plankton"]))
Ouput
sharks,crustaceans,plankton
If we want to add a comma and a space between string values in our new string, we can simply rewrite our expression with a whitespace after the comma: ", ".join(["sharks", "crustaceans", "plankton"]).

Just as we can join strings together, we can also split strings up. To do this, we will use the str.split() method:

print(balloon.split())
Ouput
['Sammy', 'has', 'a', 'balloon.']
The str.split() method returns a list of strings that are separated by whitespace if no other parameter is given.

We can also use str.split() to remove certain parts of an original string. For example, let’s remove the letter a from the string:

print(balloon.split("a"))
Ouput
['S', 'mmy h', 's ', ' b', 'lloon.']
Now the letter a has been removed and the strings have been separated where each instance of the letter a had been, with whitespace retained.

The str.replace() method can take an original string and return an updated string with some replacement.

Let’s say that the balloon that Sammy had is lost. Since Sammy no longer has this balloon, we will change the substring "has" from the original string balloon to "had" in a new string:

print(balloon.replace("has","had"))
Within the parentheses, the first substring is what we want to be replaced, and the second substring is what we are replacing that first substring with. Our output will look like this:

Ouput
Sammy had a balloon. 


# In[ ]:




Sets and its default functions
Python Set remove() : Removes Element from the Set
We can remove elements from a set by using the discard() method. Again as we have just discussed that there is no specific index attached to the newly added element in our set.
Syntax:
set.remove(element)
Python Set add() : adds element to a set

We can add elements to a set by using add() method. Remember that, there is no specific index attached.

Syntax:
set.add(elem)
Python Set copy(): Returns Shallow Copy of a Set
Syntax:

numbers = {1, 2, 3, 4}

new_numbers = numbers
Python Set clear(): remove all elements from a set
Syntax:

set.clear()
Python Set difference() : Returns Difference of Two Sets

Syntax:

A.difference(B)
Python Set difference_update() : Updates Calling Set With Intersection of Sets
Syntax:
A.difference_update(B)
Python Set discard() : Removes an Element from The Set.
Syntax:
s.discard(x)
Python Set intersection() : Returns Intersection of Two or More Sets
Syntax:
A.intersection(*other_sets)
Python Set intersection_update() : Updates Calling Set With Intersection of Sets
Syntax:
A.intersection_update(*other_sets)
Python Set isdisjoint(): Checks Disjoint Sets
Syntax:
set_a.isdisjoint(set_b)
Python Set issubset(): Checks if a Set is Subset of Another Set
Syntax:
A.issubset(B)
Python Set issuperset(): Checks if a Set is Superset of Another Set
Syntax:
A.issuperset(B)
Python Set pop() : Removes an Arbitrary Element
Syntax:
set.pop()
Python Set symmetric_difference() : Returns Symmetric Difference
Syntax:
A.symmetric_difference(B)
Python Set symmetric_difference_update() : Updates Set With Symmetric Difference
Syntax:
A.symmetric_difference_update(B)
Python Set union() : Returns Union of Sets
The union operation on two sets produces a new set containing all the distinct elements from both the sets. In the below example the element “Wed” is present in both the sets.
Syntax:
A.union(*other_sets)
Python Set update() : Add Elements to The Set.
Syntax:
A.update(B)
Python any(): Checks if any Element of an Iterable is True
Syntax:
any(iterable)
Python all(): returns true when all elements in iterable are true
Syntax:
all(iterable)
Python ascii(): Returns String Containing Printable Representation.
Syntax:
ascii(object)
Python bool(): Converts a Value to Boolean.
Syntax:
bool([value])
Python enumerate() : Returns an Enumerate Object
Syntax:
enumerate(iterable, start=0)
Python filter(): constructs iterator from elements which are true
Syntax:
filter(function, iterable)
Python frozenset() : returns immutable frozenset object.
Syntax:
frozenset([iterable])
Python iter() : returns iterator for an object.
Syntax:
iter(object[, sentinel])
Python len()  : Returns Length of an Object.
Syntax:
len(s)
Python max() : returns largest element.
Syntax:
max(iterable, *iterables[,key, default])
max(arg1, arg2, *args[, key])
Python min() : returns smallest element.
Syntax:
min(iterable, *iterables[,key, default])
min(arg1, arg2, *args[, key])
Python map() :  Applies Function and Returns a List.
Syntax:
map(function, iterable, ...)
Python set() : returns a Python set.
Syntax:
set([iterable])
Python sorted() : returns sorted list from a given iterable.
Syntax:
sorted(iterable[, key][, reverse])
Python sum() : Add items of an Iterable.
Syntax:
sum(iterable, start)
Python zip() : Returns an Iterator of Tuples.
Syntax:

zip(*iterables)
EXAMPLE PROGRAM
x={"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}
y={"Jan","Feb","Mar","Wed"}
x.discard("Sun")     #remove
print(x)
x.add("Sun")    #add
print(x)
z = x|y       #union
print(z)
w = x & y  #intersection
print(w)
a = x- y    #difference
print(a)
b= x <= y      #compare
c = y >= x
print(b)
print(c)
OUTPUT:

{'Tue', 'Sat', 'Wed', 'Mon', 'Fri', 'Thu'}
{'Tue', 'Sat', 'Wed', 'Mon', 'Fri', 'Thu', 'Sun'}
{'Jan', 'Tue', 'Feb', 'Sat', 'Wed', 'Mon', 'Mar', 'Fri', 'Thu', 'Sun'}
{'Wed'}
{'Tue', 'Sat', 'Mon', 'Fri', 'Thu', 'Sun'}
False
False 


# In[ ]:


Tuple and explore default functions
Tuples in Python
A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.

Creating Tuples

# An empty tuple

empty_tuple = ()

print (empty_tuple)
Output:

()
# Creating non-empty tuples

 
# One way of creation

tup = 'python', 'geeks'

print(tup)

 
# Another for doing the same

tup = ('python', 'geeks')

print(tup)
Output

('python', 'geeks')
('python', 'geeks')






Concatenation of Tuples

# Code for concatenating 2 tuples

 

tuple1 = (0, 1, 2, 3)

tuple2 = ('python', 'geek')

 
# Concatenating above two

print(tuple1 + tuple2)
Output:

(0, 1, 2, 3, 'python', 'geek')


Nesting of Tuples

# Code for creating nested tuples

 

tuple1 = (0, 1, 2, 3)

tuple2 = ('python', 'geek')

tuple3 = (tuple1, tuple2)

print(tuple3)
Output :

((0, 1, 2, 3), ('python', 'geek'))


Repetition in Tuples



# Code to create a tuple with repetition

 

tuple3 = ('python',)*3

print(tuple3)
Output

('python', 'python', 'python')




Immutable Tuples

#code to test that tuples are immutable

 

tuple1 = (0, 1, 2, 3)

tuple1[0] = 4

print(tuple1)



Slicing in Tuples

# code to test slicing

 

tuple1 = (0 ,1, 2, 3)

print(tuple1[1:])

print(tuple1[::-1])

print(tuple1[2:4])
Output

(1, 2, 3)
(3, 2, 1, 0)
(2, 3)


Deleting a Tuple



# Code for deleting a tuple

 

tuple3 = ( 0, 1)

del tuple3

print(tuple3)

Output:

(0, 1)


Finding Length of a Tuple

# Code for printing the length of a tuple

 

tuple2 = ('python', 'geek')

print(len(tuple2))
Output

2


Converting list to a Tuple

# Code for converting a list and a string into a tuple

 

list1 = [0, 1, 2]

print(tuple(list1))

print(tuple('python')) # string 'python'
Output

(0, 1, 2)
('p', 'y', 't', 'h', 'o', 'n')






Tuples in a loop

#python code for creating tuples in a loop

 

tup = ('geek',)

n = 5  #Number of time loop runs

for i in range(int(n)):

    tup = (tup,)

    print(tup)
Output :

(('geek',),)
((('geek',),),)
(((('geek',),),),)
((((('geek',),),),),)
(((((('geek',),),),),),)


Using cmp(), max() , min()

# A python program to demonstrate the use of 
# cmp(), max(), min()

 

tuple1 = ('python', 'geek')

tuple2 = ('coder', 1)

 

if (cmp(tuple1, tuple2) != 0):

 

    # cmp() returns 0 if matched, 1 when not tuple1 

    # is longer and -1 when tuple1 is shoter

    print('Not the same')

else:

    print('Same')

print ('Maximum element in tuples 1,2: ' +

        str(max(tuple1)) +  ',' +

        str(max(tuple2)))

print ('Minimum element in tuples 1,2: ' +

     str(min(tuple1)) + ','  + str(min(tuple2)))
Output

Not the same
Maximum element in tuples 1,2: python,coder
Minimum element in tuples 1,2: geek,1 


# In[ ]:




List and its default functions


Adding and Appending

1.append(): Used for appending and adding elements to List.It is used to add elements to the last position of List.
Syntax:
list.append (element)
List = ['Mathematics', 'chemistry', 1997, 2000]
List.append(20544)
print(List)
Output:
['Mathematics', 'chemistry', 1997, 2000, 20544]


2.insert(): Inserts an elements at specified position.
Syntax:

list.insert(<position, element)
Note: Position mentioned should be within the range of List, as in this case between 0 and 4, elsewise would throw IndexError.


List = ['Mathematics', 'chemistry', 1997, 2000]
# Insert at index 2 value 10087

List.insert(2,10087)     

print(List)        
Output:

['Mathematics', 'chemistry', 10087, 1997, 2000, 20544]
extend(): Adds contents to List2 to the end of List1.
Syntax:
List1.extend(List2)

List1 = [1, 2, 3]

List2 = [2, 3, 4, 5]
List1.extend(List2)        
print(List1)
List2.extend(List1) 
print(List2)
Output:
[1, 2, 3, 2, 3, 4, 5]
[2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]
sum(), count(), index(), min() and max() functions of List

3.sum() : Calculates sum of all the elements of List.
Syntax:
sum(List)
List = [1, 2, 3, 4, 5]

print(sum(List))
Output :15

4.count():Calculates total occurrence of given element of List.
Syntax:
List.count(element)

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]

print(List.count(1))
Output:
4

5.length:Calculates total length of List.
Syntax:
len(list_name)

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]

print(len(List))
Output:
10

6.index(): Returns the index of first occurrence. Start and End index are not necessary parameters.
Syntax:
List.index(element[,start[,end]])
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]

print(List.index(2))
Output:
1

7.min() : Calculates minimum of all the elements of List.
Syntax:
min(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

print(min(List))
Output:
1.054

8.max(): Calculates maximum of all the elements of List.
Syntax:
max(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

print(max(List))
Output:

5.33
sort() and reverse() functions

9.reverse(): Sort the given data structure (both tuple and list) in ascending order. Key and reverse_flag are not necessary parameter and reverse_flag is set to False, if nothing is passed through sorted().
Syntax:
sorted([list[,key[,Reverse_Flag]]])
list.sort([key,[Reverse_flag]])

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

 
#Reverse flag is set True
List.sort(reverse=True) 
#List.sort().reverse(), reverses the sorted list  

print(List)        
Output:

[5.33, 4.445, 3, 2.5, 2.3, 1.054]

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

sorted(List)

print(List)
Output:

[1.054, 2.3, 2.5, 3, 4.445, 5.33]
Deletion of List Elements

9.pop(): Index is not a necessary parameter, if not mentioned takes the last index.
Syntax:
list.pop([index])
Note: Index must be in range of the List, elsewise IndexErrors occurs.


List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

print(List.pop())
Output:

2.5

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

print(List.pop(0))
Output:
2.3

10.del() : Element to be deleted is mentioned using list name and index.
Syntax:
del list.[index]

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

del List[0]

print(List)
Output:

[4.445, 3, 5.33, 1.054, 2.5]

11.remove(): Element to be deleted is mentioned using list name and element.
Syntax:
list.remove(element)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

List.remove(3)

print(List)
Output:

[2.3, 4.445, 5.33, 1.054, 2.5]




 


# In[ ]:




Dictionary and its default functions
keys()
The method keys() returns a list of all the available keys in the dictionary.
dict={'Name':'Harry','Rollno':30,'Dept':'cse','Marks':97}

Output
dict_keys(['Name', 'Rollno', 'Dept', 'Marks'])

values()
This method returns list of dictionary dictionary's values from the list
dict={'Name':'Harry','Rollno':30,'Dept':'cse','Marks':97}
print(dict.values())
Output
dict_values(['Harry', 30, 'cse', 97])

pop()
The method pop(key) Removes and returns the value of specified key.
dict={'Name':'Harry','Rollno':30,'Dept':'cse','Marks':97}
dict.pop('Marks')
print(dict)
Output
{'Name': 'Harry', 'Rollno': 30, 'Dept': 'cse'}


get()
This method returns value of given key or None as default if key is not in the
dict={'Name':'Harry','Rollno':30,'Dept':'cse','Marks':97}
print('\nName: ', dict.get('Name'))
print('\nAge: ', dict.get('Age'))
Output
Name: Harry
Age: None

update()
The update() inserts new item to the dictionary.
dict={'Name':'Harry','Rollno':30,'Dept':'cse','Marks':97}
dict.update({'Age':22})
print(dict)
Output
{'Name': 'Harry', 'Rollno': 30, 'Dept','cse''Marla's,97,22}  

