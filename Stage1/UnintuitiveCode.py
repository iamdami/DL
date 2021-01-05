import numpy as np 
a = np.random.randn(5) # 5 Gaussian distribution values 
print(a) 
print() 

print(a.shape) # The size of a 
print() 
print(a.T) # The transpose of a is the same as a 
print() 

print(np.dot(a, a.T)) # dot product of a transpose and a 
print()
