'''
Find the minimum among 10 numbers.
Sample Testcase :
INPUT
5 4 3 2 1 7 6 10 8 9
OUTPUT
1
'''

a=list(map(int,input().split()))
min=a[0]
for i in a:
    if i<=min:
        min=i
print(min)