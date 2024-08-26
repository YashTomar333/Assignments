'''Q3. Given an array arr[] of n integers, construct a Product Array
       prod[] (of the same size) such that prod[i] is equal to the 
       product of all the elements of arr[] except arr[i].
'''


arr = []
n = int(input("Enter no. of elements u want in a list "))
for i in range(0,n):
    num = int(input("enter numbers "))
    arr.append(num)
print(arr)

pd = []

for i in arr:
    ls = arr.copy()
    prod = 1

    ls.remove(i)
    # print(ls)

    for j in ls:
        prod = prod * j

    pd.append(prod)

print("Resultant array is", pd)
