'''
Given 3 numbers A,B,C process and print 'yes' if they can form the sides of a triangle otherwise print 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes

'''

a=list(map(int,input().split()))
if a[0]+a[1]>a[2] and a[0]+a[2]>a[1] and a[1]+a[2]>a[0]:
    print('yes')
else:
    print('no')
    