'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

	
# A short way to remember LC is:

#result  = [*transform/expression*    *iteration*         *filter/condition*     ]

list1 = list(range(1,11))
list2 = []

for x in list1:
    if x > 5:
        x *= 20
        list2.append(x)
print(list2)


list2 = [x*20 for x in list1 if x > 5]
print(list2)

squares = [x ** 2 for x in range(1,11)]
print(squares)

list1 = [3,4,5]
multiplied = [item * 3 for item in list1]
print(multiplied)

listofwords = ['This', 'is', 'a', 'list', 'of', 'words']
items = [word[0] for word in listofwords]
print(items)

upper = [x.upper() for x in ['a', 'b', 'c']]
print(upper)

lower = [x.lower() for x in upper]
print(lower)

range = [i*i for i in range(10) if i % 2 == 0]
print (range)

string = "Hello 12345 world"
numbers = [int(x) for x in string if x.isdigit()]
print (numbers)

# Trad

for x in string:
    if x.isdigit():
        numbers.append(int(x))
print(numbers)

numbers = [x for x in string if x.isalpha()]
print (numbers)

infile = open("test.txt", "r")
result = [i.rstrip('\n') for i in infile if "line 3" in i]
print(result)

def double(y):
    return y*2

print(double(10))

newlist = [x + y for x in [10, 20, 50] for y in [20, 40, 60]]
print(newlist)

#doublelist = [double(y) for y in range(10) if y % 2 == 1]
#print (doublelist)








