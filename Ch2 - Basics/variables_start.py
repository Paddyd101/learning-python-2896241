# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = "abc"
print(myint)

# to access a member of a sequence type, use []
print(mylist[2])
print(mytuple[1])


# use slices to get parts of a sequence
print(mylist[1:4])
print(mylist[1:4:2])

# you can use slices to reverse a sequence [::-1]
print(mylist)
print(mylist[::-1])

# dictionaries are accessed via keys
print(mydict["one"])

# ERROR: variables of different types cannot be combined
#print("string" +123) not allowed
#print (int("String")+4) not allowed

#print("123"+str(4)) is allowed
print(int("123")+4) #is allowed

# Global vs. local variables in functions
def someFunc():
	#run this by commenting and uncommenting the global line below
	global mystr
	mystr = "def"
	print(mystr)

someFunc()
print(mystr)


##deletes variable definitong
del mystr
print(mystr)
