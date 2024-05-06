Sets and Dictionaries:

Sets are a built-in data type where elements inside  only occur once.

It is defined with curly braces { }
You can transform a list into a set using a set constructor:
set()

set.add(element) => add an element to a set
set.remove(element) => removes an element
set.discard(element) => removes an element without raising an error if element is not found
ser.pop(): returns a random number in set
set.clear(): clears a set
set.copy(): makes a shallow copy of set
Set.union(set 2) or  set1 | set 2: unites two sets
Set.intersection(): make a new set with common elements in both sets 
Set.difference() or - : make a new set with the unique elements in set 1
set.symmetric_difference(): make a new set with unique elements in set 1 and 2
_____________________________________________
Dictionary:
Stores a collection of key-value pairs in the following syntax:
{“key1”:”value1”}
Also use dict() constructor

To access a value in a dictionary call it by it’s key’s name
Eg:  name = my_dictionary[“name”]

You can also add new keys/update values

To remove an item use .pop
Or del mydictionary
.get() => 

To iterate over keys:
For I in new:
	print(key) #without “ “

To iterate over values in loop:
For i in dictionary.values():
print(i)

To iterate over both
For x,y in mydict.items():
	print(x, y)

Lambda function:
An anonymous inline function that can have any number of arguments but can only have one expression

Written in form:
Lambda  (arguments): (expression)

Eg: add = lambda x, y: x + y

MAPS:
map(function, sequence)

Takes a function and a sequence (such as list) and returns a new sequence containing the results of the function on the original sequence

Eg: sq = map(lambda x: x**2, numberslist)


Filter:
filter(function, sequence) based on whether the item inside the sequence satisfies the condition inside the function or not, the item passes the filter\.

Function used must have a boolean return type.


Reduce:
reduce(function, sequence):
Used to take all elements inside a sequence and makes them into one single product
Eg:
reduce(lambda x,y: x * y, numbers) ⇒ (1 * 2 * 3 * 4 * 5)
