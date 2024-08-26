'''Q4. Given a sorted array arr[] (may be distinct or may contain duplicates)
        of size N that is rotated at some unknown point, the task is to find
        the minimum element in it.
'''


arr = []
n = int(input("Enter no. of elements u want in a list "))
for i in range(0,n):
    num = int(input("enter numbers "))
    arr.append(num)
print(arr)

# print(min(arr))
temp = 0

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

for j in range(len(arr)-1):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=swap(arr[i],arr[i+1])

print(arr)

print("<inimum of arr[] is", arr[0])