'''
Given a number N followed by N numbers.Find the smallest number and largest number and print both the indices(1 based indexing).
Input Size : N <= 100000
Sample Testcase :
INPUT
5
1 2 3 4 5
OUTPUT
1 5

'''
a=int(input())
b=list(map(int,input().split()))
c=sorted(b)
minb=c[0]
maxb=c[-1]
print(b.index(minb)+1,b.index(maxb)+1)