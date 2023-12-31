class recursion:
    @staticmethod   
    def factorial(n:int):
        """Compute the factorial of a specified number. 

        Args:
            n (int): specified number; for example, 6 

        Returns:
            int: computed factorial 
        """ 
        # this is the stopping case 
        if (n == 1):
            return n 
        else: 
            # this is the general rule that includes the 
            # recursive call 
            return n * recursion.factorial(n-1)
        

    @staticmethod
    def power(number: int, power: int):
        """Takes a specified number to a specified power.

        Args:
            number (int): specified number; for example, 2
            power (int): specified power; for example, 5

        Returns: 
            int: computed power
        """     
        # the counter variable for the loop contains the 
        # same value as power 

        # the loop will repeat as long as i > 1 
        # the condition that will cause the loop to stop 
        # is when i == 1 -> stopping case for the loop 


        # with each iteration of the loop, we're decrementing 
        # the counter variable by 1   

        if power == 0:
            return 1 
        else: 
            return number * recursion.power(number,power - 1)
        
    @staticmethod
    def computeMin(nums, i: int, min: int):
        """Finds the minimum number is a specified list of numbers.

        Args:
            nums: specified list

        Returns:
            int: minimum number
        """
        if (i == len(nums)):
            return min 
        else:
            if (nums[i] <= min):
                min = nums[i]
            return recursion.computeMin(nums,i + 1,min)
           
    @staticmethod
    def reverse(s:str, i: int):
        """Displays a specified string in reverse. 

        Args:
            s (str): specified string
        """        
        if (i == 0):
            print("is the reverse of %s using a recursion"%(s))
        else:
            print(s[i-1],end=" ")
            recursion.reverse(s,i-1)
    @staticmethod

    def search (a, first: int, size: int, target, i: int, found: bool):
        """Searches for a desired element in a list of elements
        starting at a[first].

        Args:
        a: the list to search
        first (int): the list index at which the search will start
        size (int): the number of elements to search
        target: the element to search for
        i: the counter variable used to iterate through list
        found: the variable used to denote if the target has been found

        Returns:
        int: If target appears in the list, index of the element
        that contains the target, else -1.
        """
        if ((i == size) or found or (i+first == len(a))):
            if (found):
                return i + first
            else: 
                return -1 
        else: 
            if (a[i + first] == target):
                return recursion.search(a,first,size,target,i,True)
            else:
                return recursion.search(a,first,size,target,i+1,False)
            


        

        