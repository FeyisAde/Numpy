## Numpy Exercise
import numpy as np 

## Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
twos = np.full((4,3),2)
print(twos)
print()

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
numbers = np.arange(0, 111, 10).reshape(3,4)
print(numbers)
print() 

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")
numbers1 = np.arange(0, 111, 10).reshape(4,3)
print(numbers1)
print()

## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
numbers3 = numbers1 *  3
print(numbers3)
print()

## Step 5: Multiply your array from step one by your array from step 2
print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")
# twosnos = twos * numbers
# print(twosnos)
## This errored out... why? Because you cannot perform calculation on arrays with two different sizes. 
# Step one is a 4x3 while Step two is a 3x4
print()

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")
numbers6 = twos * numbers1
print(numbers6)
## this worked! why? Because both arrays are thesame size 4x3
print()



