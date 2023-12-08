from recursions import  *

print("Recursion")
a = list(map(int,input("Enter seven numbers seperated by space: ").split()))

    # Prompt the user for the index at which the search will begin 
first = int(input("Enter the index at which the search will begin: "))

    # Prompt the user for the number of elements to search 
size = int(input("Enter the size of the list that will be searched: "))

    # Prompt the user for the target
target = int(input("Enter the target value to search for: "))

# Call search and display its return
if (recursion.search(a,first,size,target,0,False)==int):
    print("Target found at index....",recursion.search(a,first,size,target,0,False))
else:
    print(f"{target} not found")