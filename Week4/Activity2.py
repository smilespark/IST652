# Create a four-by-five numpy array 
import numpy as np

my_array = np.array([[1, 2, 3, 4, 5], 
                     [6, 7, 8, 9, 10], 
                     [11, 12, 13, 14, 15], 
                     [16, 17, 18, 19, 20]])

# Use index slicing two get the last two rows and third and fourth columns
sliced_array = my_array[2:, 3:]
print(sliced_array)

# Create a one dimensional array that sums all the columns
array_sum = [sum(x) for x in zip(*my_array)]
print(array_sum)