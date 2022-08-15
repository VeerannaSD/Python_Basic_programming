'''
Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), if it is not possible to select coins in such a way that they sum up to S then print '-1'.
Example: Given coins with values 1, 3, and 5. And the sum S is 11.
Output: 3, 2 coins of 3 and 1 coin of 5
Input Size : N<=10000
Example:
INPUT
3 11
1 3 5
OUTPUT
3
'''
import sys

def min_coins(coins,no_of_coins,min_sum):
    table=[i for i in range(min_sum+1)]
    table[0]=0
    for i in range(1,min_sum):
        table[i]=sys.maxsize
    for i in range(1,min_sum+1):
        for j in range(no_of_coins):
            if coins[j]<=i:
                sub_res=table[i-coins[j]]
            if (sub_res!=sys.maxsize and sub_res+1<table[i]):
                table[i]=sub_res+1
    if table[min_sum]==sys.maxsize:
        return -1
    return table[min_sum]
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(min_coins(b,len(b),a[1]))