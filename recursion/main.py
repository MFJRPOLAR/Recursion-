from loops import * 
from recursions import  *

print("Factorial of 6 using a loop is:", loops.factorial(6))
print("Factorial of 5 using a loop is:", loops.factorial(5))
print("Factorial of 4 using a loop is:", loops.factorial(1))


print("Factorial of 6 using a recursion is:", recursion.factorial(6))
print("Factorial of 5 using a recursion is:", recursion.factorial(5))
print("Factorial of 4 using a recursion is:", recursion.factorial(1))

print("2 to the 5th power using a loop is:", loops.power(2,5))
print("2 to the 4th power using a loop is:", loops.power(2,4))
print("2 to the 0 power using a loop is:", loops.power(2,0))

print("2 to the 5th power using a recursion is:", recursion.power(2,5))
print("2 to the 4th power using a recursion is:", recursion.power(2,4))
print("2 to the 0 power using a recursion is:", recursion.power(2,0))


nums = [5,12,3,4]
print("Minimum number using a loop is: ", loops.computeMin(nums))
print("Minimum number using a recursion is: ", recursion.computeMin(nums,0,nums[0]))

word = "TAC"
loops.reverse(word)
recursion.reverse(word,len(word))

print("Loop")
a = [-7,42,70,39,3,63,8]

# Prompt the user for the index at which the search will begin 
first = 0

    # Prompt the user for the number of elements to search 
size = 10

    # Prompt the user for the target
target = 39

# Call search and display its return
print("Target found at index....",loops.search(a,first,size,target))


print("Recursion")
# Call search and display its return
if (recursion.search(a,first,size,target,0,False)== -1):
    print(f"{target} not found")
else:
    print("Target found at index....",recursion.search(a,first,size,target,0,False))