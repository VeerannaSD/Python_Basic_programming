'''
Given base(B) and height(H) of a triangle find its area.
Input Size : N <= 1000000
Sample Testcase :
INPUT
2 4
OUTPUT
4
'''
a=list(map(int,input().split()))
print('Area of triangle:',1/2*a[0]*a[1])