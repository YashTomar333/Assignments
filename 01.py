''' Q1-> Given an array A [] of n numbers and another number x, the task
         is to check whether or not there exist two elements in A [] whose
         sum is exactly x. '''


A =[]
n = int(input("Enter no. of elements u want in a list "))
for i in range(0,n):
    num = int(input("enter element "))
    A.append(num)
print(A)


x = int(input("Enter number (x)"))
print(x)


flag = False

for i in A:
    temp = i
    # print(temp)

    ls1=A.copy()
    ls1.remove(temp)
    # print(ls1)

    for j in ls1:
        req_num = x - temp
        if req_num in ls1:
            flag =True
        if flag == True:
            break
    if flag == True:
        break
print("Result:", flag, "\n", "numbers are", temp, req_num )