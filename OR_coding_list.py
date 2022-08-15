'''
Given a number N and an array of N elements, find the Bitwise OR of the array elements.
Input Size : N <= 100000
Sample Testcase :
INPUT
2
2 4
OUTPUT
6
'''

n=int(input())
a=list(map(int,input().split()))
ans=a[0]
for i in range(1,len(a)):
    ans=ans|a[i]
print(ans)