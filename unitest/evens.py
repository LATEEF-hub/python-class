def even_num_of_evens(numbers):
    """
    Should raise TypeError if a list is not passed into the function
    error message: "A list was not passed into the function"
    if the number of even numbers is odd, return False
    if the number of even numbers is 0, return False
    if the number of even numbers is even, return True
    """
    if isinstance(numbers, list):
        return True
    else:
        raise TypeError("A list was not passed into the function, please check function!")

if __name__ == '__main__':
    print(even_num_of_evens(5))