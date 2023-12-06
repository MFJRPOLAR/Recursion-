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