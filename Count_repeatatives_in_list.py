'''
Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
Sample Testcase :
INPUT
6 2
1 2 3 5 7 8
OUTPUT
0
'''
a=list(map(int,input().split()))
b=list(map(int,input().split()))

if a[1] not in b:
    print(-1)
else:
    if a[1] in b:
        print(b.count(a[1])-1)
        
        