'''
Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
Sample Testcase :
INPUT
4 2
1 2 3 3
OUTPUT
yes
'''
a,b = input().split()
c=list(map(int, input().split()))
inta= int(a)
intb= int(b)

if intb in c:
   print('yes')
else:
   print('no')