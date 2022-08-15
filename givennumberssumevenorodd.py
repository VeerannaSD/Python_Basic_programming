'''
Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
Sample Testcase :
INPUT
9 2
OUTPUT
odd
'''
a=list(map(int,input().split()))
suma=sum(a)
if suma%2==0:
    print('even')
else:
    print('odd')