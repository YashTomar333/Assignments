'''Q2. Given an array prices[] of length N, representing
       the prices of the stocks on different days, the
       task is to find the maximum profit possible by 
       buying and selling the stocks on different days
       when at most one transaction is allowed.
Note: Stock must be bought before being sold.
'''



prices = []
n = int(input("Enter no. of elements u want in a list "))
for i in range(0,n):
    num = int(input("enter price of stock "))
    prices.append(num)
print(prices)

sell = 0
buy = 0

ls = prices.copy()
# print(ls)
max_profit = 0

for i in prices[0:n-1]:
    temp = i
    ls.remove(temp)
    # print(ls)
    a = max(ls)
    profit = a - temp
    if max_profit < profit:
        max_profit = profit
        sell = a
        buy = temp
print("Max Profit is", max_profit, "\n","Buy at price", buy, "And sell at price",sell )


    

