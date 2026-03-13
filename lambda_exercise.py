''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

original_list = list(range(1,11))
print (original_list)
even_list = list(filter(lambda num: (num % 2 == 0), original_list))
print(even_list)
odd_list = list(filter(lambda num: (num % 2 == 1), original_list))
print(odd_list)


''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

sixchar = list(filter(lambda char: len(char) == 6, weekdays))
print(sixchar)









''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

orig_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_list = ['orange', 'black']

new_list = list(filter(lambda word: word not in remove_list, orig_list))
print(new_list)
                





''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

cust_list = list(filter(lambda num: num not in list2, list1))
print(cust_list)






''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
original_list = ['red', 'black', 'white', 'green', 'orange']

ack_list = list(filter(lambda x: 'ack' in x, original_list))
print (ack_list)

abc_list = list(filter(lambda x: 'abc' in x, original_list))
print (abc_list)

''' 6)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_list = sorted(original_scores, key = lambda x: x[1])
print(sorted_list)
# OR
original_scores.sort(key = lambda x: x[1])


''' 7)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful). Use all three of the below
varaitions (str1, str2, str3) to check if your program works. It should FAIL for str1 and str2 and PASS for str3.
'''

str1 = "HELLO"
str2 = "hello"
str3= "Hello8world"

result1 = [x.isupper() for x in str1]
result2 = [x.islower() for x in str2]
result3 = [x.isdigit() for x in str3]
print(result1)
print(result2)
print(result3)

result = lambda somestring: any ([x.isupper() for x in somestring]
        and [x.isupper() for x in somestring]
        and [x.isdigit() for x in somestring]
        and [len(somestring) > 7])
if result(str2):
    print("pass")
else:
    print("fail")