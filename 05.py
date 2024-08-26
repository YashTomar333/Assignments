'''Q5. Given an array of N integers where each value
       represents the number of chocolates in a packet.
       Each packet can have a variable number of 
       chocolates. There are m students, the task is
       to distribute chocolate packets such that: 
•	Each student gets one packet.
•	The difference between the number of chocolates in 
    the packet with maximum chocolates and the packet
    with minimum chocolates given to the students is minimum'''



pac = []
n = int(input("Enter no. of elements u want in a list "))
for i in range(0,n):
    num = int(input("enter numbers "))
    pac.append(num)
print(pac)

m = int(input("Enter no. of students"))

pac.sort()
diff = 0
min_diff = 1000000
min_c = 0
max_c = 0

i = 0
for i in range(n-(m-1)):
    # print(n-(m-1))
    # print(pac[i])
    # print(pac[(i+(m-1))])
    r = i+(m-1)
    print(r)
    diff = (pac[r] - pac[i])

    if diff < min_diff:
        min_diff = diff
        min_c = pac[i]
        max_c = pac[r]


print("Minimum difference is", min_diff)
print("Minimum chocolate given to student is", min_c)
print("Maximum chocolate given to student is", max_c)


