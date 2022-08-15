'''
Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.
Sample Testcase :
INPUT
3
2 6
OUTPUT
yes
'''
n=int(input())
a=list(map(int,input().split()))
l=a[0]
r=a[1]

if n>l & n<r:
    print('yes')
else:
    print('no')