import numpy as np

# data
A = np.array([[56.0, 0.0, 4.4, 68.0],
              [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])

print(A)
print()

# add the sum of each column
cal = A.sum(axis=0)  # add vertically
print(cal)
print()

# compute the percentage
# An example of broadcasting(reshape())
percentage = 100 * A / cal.reshape(1, 4)  # It's a percentage, you have to multiply by 100
print(percentage)
