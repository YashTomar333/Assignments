ls =[]
n = int(input("Enter no. of elements u want in a list "))
for i in range(0,n):
    x = int(input("enter element "))
    ls.append(x)
print(ls)


num = int(input("Enter number (num)"))
print(num)


flag = False

for i in ls:
    temp = i
    # print(temp)

    ls1=ls.copy()
    ls1.remove(temp)
    # print(ls1)

    for j in ls1:
        req_num = num - temp
        if req_num in ls1:
            flag =True
        if flag == True:
            break
    if flag == True:
        break
print("Result:", flag, "\n", "numbers are", temp, req_num )