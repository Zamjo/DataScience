import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])
b = np.array([1, 2, 3])
print("First array:")
print(a)
print("Second array")
print(b)
print("\n")
print("Append elements to array:")
print("\n2darray")
print(np.append(a, [7, 8, 9]).reshape(3, 3))
print("\n1darray:")
print(np.append(b, [7, 8, 9]))
