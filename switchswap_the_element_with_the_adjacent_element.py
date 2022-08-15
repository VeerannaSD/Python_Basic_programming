'''
Given an array of N elements switch(swap) the element with the adjacent element and print the output.
Sample Testcase :
INPUT
5
3 2 1 2 3
OUTPUT
2 3 2 1 3
'''

a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(0,len(b),2):
    #print(i,b[i])
    if i+1>=len(b):
        c.append(b[i])
        break
    c.append(b[i+1])
    c.append(b[i])

print(*c) 