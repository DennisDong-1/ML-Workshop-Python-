import numpy as np

# a = n.array([1, 2, 3], dtype=n.uint32)
# b = n.array([4, 5, 6], dtype=n.uint32)

# c_unsigned32 = a - b
# print("Unsigned: ", c_unsigned32, c_unsigned32.dtype)

# c_signed32 = a - b.astype(n.int32)
# print("Signed ", c_signed32, c_unsigned32.dtype)

# arr1 = np.arange(10, 20, 2, dtype=np.uint32)
# print(arr1)

# arr_of_floats = np.linspace(0, 0.2, 3, dtype=np.float32)
# print(arr_of_floats)

# random_arr = np.random.rand(4, 4)
# print(random_arr)

arr2 = np.array([[41, 22, 39, 45],
                [62, 17, 81, 910],
                [42, 17, 83, 41],
                [67, 62, 147, 22]])

# print(arr2)

# print(arr2[0][0])
# print(arr2[: , :])

# print(arr2[2, 2])

# print(arr2[1:4,1:4])

# print(arr2[2:3, 1:3])

# np.random.seed(0)

# arr = np.random.randint(1, 100, size = (4, 4))
# print("Original array: ", arr)
# print("Boolean indexed array: ", arr[arr > 50]) #Boolean masking
# print("Boolean indexed array: ", [arr > 50]) #Boolean masking

# var = np.where( arr > 50)
# print(var)

array_a = np.array([[1, 2, 3],
                    [4, 5, 6]])

array_b = array_a

array_b[1][1] = 100

print(array_a)

array_c = np.copy(array_a)
print(array_c)

#Task to do - 