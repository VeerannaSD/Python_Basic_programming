'''
Given 3 numbers A,B,C print 'yes' if they can form the sides of a right angled triangle,otherwise 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes
'''

a=list(map(int,input().split()))
if a[0]**2+a[1]**2==a[2]**2:
    print('yes')
else:
    print('no')