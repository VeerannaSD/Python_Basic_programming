'''
Write a code to get a integer n as input and calculate the smallest perfect power of 2 greater than n.

Input Description:
A single line containing an integer,n.

Output Description:
Print the smallest perfect power of 2 greater than n.

Sample Input :
48
Sample Output :
64

'''
n=int(input())
for i in range(2,n):
    b=2**i
    if b>n:
        break
print(b)