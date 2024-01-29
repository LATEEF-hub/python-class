def even_num_of_evens(numbers):
    """
    Should raise TypeError if a list is not passed into the function
    error message: "A list was not passed into the function"
    if the number of even numbers is odd, return False
    if the number of even numbers is 0, return False
    if the number of even numbers is even, return True
    """
    #Method : Write a test that fails then add a code to the function that will make it pass
    # using isinstance method to check 
    # if the value entered is a list
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])
        
        return True if evens and evens % 2 == 0 else False

        # if numbers == []:
        #     return False
        # else:
        #     evens = 0
        # for n in numbers:
        #     if n % 2 == 0:
        #         evens += 1

        # if evens:
        #     return evens % 2 == 0
        # else:
        #     return False          
    else:
        raise TypeError("A list was not passed into the function, please check function!")

if __name__ == '__main__':
    even_num_of_evens([5,3,4])