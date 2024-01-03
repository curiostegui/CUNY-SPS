'''
Assignment #5
1. Add / modify code ONLY between the marked areas (i.e. "Place code below") 
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 05_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
'''

import numpy as np, pandas as pd

#--- Exercise responses ---#

def exercise01():
    '''
    Create a DataFrame df with 4 columns and 3 rows of data in one line of code. The data can be arbitrary integers.
    For example
    
               0  1  2   3
            0  1  2  3   4
            1  5  6  7   8
            2  7  8  9  10
    '''
df = pd.DataFrame([[1,2,3,4],[5,6,7,8],[7,8,9,10]])
return df

df = exercise01()
  
------------------------
def exercise02(a):
    # The function exercise02() receives a Python list and converts it to an ndarray. Convert the list to a numpy ndarray called array.
    array = np.array(a)
    return array

# Test cases
test_cases = [
    [],  # Empty list
    [1, 2, 3],  # List of integers
    [1.1, 2.2, 3.3],  # List of floats
    [[1, 2], [3, 4]],  # Nested list (2D array)
    ["a", "b", "c"],  # List of strings
    [True, False, True]  # List of booleans
]

# Testing the function
for i, test in enumerate(test_cases):
    result = exercise02(test)
    print(f"Test Case {i+1}: Input: {test} | Output: {result} | Type: {type(result)}")    

------------------------
def exercise03(a):
    # The function exercise03() receives an ndarray of integers. Return the sum of those integers using NumPy.
    
    if not isinstance(a, np.ndarray):
        raise TypeError("Input should be NumPy ndarray")
    if a.dtype != np.int:
        raise TypeError("Input should be ndarray of integers")
    
    sum = np.sum(a)
    return sum

    
test_array = np.array([1, 2, 3, 4])
exercise03(test_array)
   
    
------------------------
def exercise04(a):
    # The function exercise04() receives an ndarray matrix (2D) of integers. Return the sum of the 2nd column using NumPy.
    sum = np.sum(a[:, 1])
    return sum

 # Test cases
test_matrices = [
    np.array([[1, 2], [3, 4], [5, 6]]),  # 3x2 matrix
    np.array([[10, 20, 30], [40, 50, 60]]),  # 2x3 matrix
    np.array([[1, 2], [3, 4]]),  # 2x2 matrix
    np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])  # 3x4 matrix
]

# Testing the function
for i, test_matrix in enumerate(test_matrices):
    result = exercise04(test_matrix)
    print(f"Test Case {i+1}: Sum of 2nd column: {result}")  
    

------------------------
def exercise05(n):
    # The function exercise05() receives an integer n. Return an ndarray filled with zeros of size n x n (n rows, n columns)
    zeros = np.zeros((n,n))
    return zeros

# Test cases
test_cases = [0, 1, 2, 5, 10]  # Different sizes of n

# Testing the function
for n in test_cases:
    result = exercise05(n)
    print(f"Test Case (n={n}):")
    print(result)
    print()

------------------------    
def exercise06(n):
    # The function exercise06() receives an integer n. Return an ndarray filled with ones of size n x n (n rows, n columns)
    ones = np.ones((n,n))
    return ones

# Test cases
test_cases = [0, 1, 3, 5]  # Different sizes of n

# Testing the function
for n in test_cases:
    result = exercise06(n)
    print(f"Test Case (n={n}):")
    print(result)
    print()

------------------------    
def exercise07(sd,m,s):
    # The function exercise07() receives integers sd, m, s which are standard deviation, mean and size respectively. 
    # Return an ndarray filled with s random numbers conforming to a normal distribution of standard deviation = sd and mean = m
    random_numbers = np.random.normal(loc=m, scale=sd, size=(s,))
    return random_numbers

# Test cases
test_params = [
    (1, 0, 5),  # Standard deviation 1, mean 0, size 5
    (2, 10, 3),  # Standard deviation 2, mean 10, size 3
    (0.5, -2, 10)  # Standard deviation 0.5, mean -2, size 10
]

# Testing the function
for i, (sd, m, s) in enumerate(test_params):
    result = exercise07(sd, m, s)
    print(f"Test Case {i+1}: SD={sd}, Mean={m}, Size={s}")
    print(result)
    print()





