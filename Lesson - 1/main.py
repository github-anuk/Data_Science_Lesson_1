import numpy as np

lists=[0,2,3,4,5,6]

print(type(lists))

aray=np.array(lists)
print(type(aray))

#error=np.array([1,"ERROR HERE","abccc",2,3,4],"eroor")
#print(error)

nums=np.array([1,2,3,4,5,6,7,8,9,0])
nums*=10
print(nums)
aray0=np.zeros(10)
print(aray0)

array1=np.ones(10)
print(array1)

ar=np.array([2,3,4,9,5,6,7],dtype = "f")
print(ar)

rar=np.array([[1,3],[2,4]])
print(rar)

#rawr=np.array([[1,3],[2]])
#print(rawr)

print("ARRARY DIMENSION",rar.ndim)
print("NUMBER OF ROWS N COLOUMNS ", rar.shape)
print("NUMBER OF ELEMENTS",rar.size)
print("ARRAY SIZE",rar.nbytes)

num_array=np.arange(1,100)
print(num_array)


nwum_array=np.arange(2,100,2)
print(nwum_array)
randome_RAR=np.random.permutation(np.arange(1,11))
print("PERMUTATION: ",randome_RAR)

randomeeeee_NUM=np.random.randint(1,200)
print(randomeeeee_NUM)

rand_n=np.random.rand(1,20)
print(rand_n)

reshaped_RAR=np.arange(1,10).reshape(3,3)
print(reshaped_RAR)