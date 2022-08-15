
'''
Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
Sample Testcase :
INPUT
5 5
OUTPUT
yes
'''
a=list(map(int,input().split()))#Get user input in list a

if a[0]==a[1]:#check given numbers in list are same
    print('yes')
else:
    print('no')