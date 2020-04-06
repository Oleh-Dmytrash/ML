import numpy as np

arr = np.zeros(10)
print(arr)

arr = np.ones(10)
print(arr)

arr = np.full(shape=10,fill_value=2.5)
print(arr)

arr = np.zeros(10)
arr[4]= 1
print(arr)

arr = np.arange(10,50)
print(arr)

arr = arr[::-1]
print(arr)

arr = np.arange(9).reshape(3,3)
print(arr)

arr = np.nonzero([1,2,0,0,4,0])
print(arr)

arr = np.eye(3)
print(arr)

arr = np.random.uniform((3,3,3))
print(arr)

arr = np.random.random((10,10))
arr_min = arr.min()
arr_max = arr.max()
print(arr)

arr = np.random.random(30)
mean_val = arr.mean()
print(arr)

arr = np.ones((5,5))
arr[1:-1,1:-1]=0
print(arr)

arr = np.diag(1+np.arange(4), k = -1)
print(arr)

arr = Z = np.zeros ((8,8), dtype=int)
arr[1::2, ::2]= 1
arr[::2, 1::2] = 1
print(arr)

index = np.unravel_index(100, (6,7,8))
print(arr)

arr = np.array([[0,1], [1,0]])
res_arr = np.tile(arr,(4,4))
print(arr)

arr = np.dot(np.ones((5,3)), np.ones((3,2)))
print(arr)

arr = np.arange(0, 10)
arr[(arr > 3)&(arr < 8)] = -arr[(arr > 3)&(arr < 8)]
print(arr)

arr = np.zeros((5,5))
arr += np.arange(5)
print(arr)
