'''
Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.

Input Description:
A single line containing 2 integers separated by space.

Output Description:
Print the HCF of the integers.

Sample Input :
2 3
Sample Output :
1
'''

A,B = map(int,input().split(' '))
#print(A,B)

if A>B:
    divident = A
    divisor = B
else:
    divident = B
    divisor = A
#print(divident , divisor)

while True:
    q = divident // divisor #130 //91  1
    r = divident % divisor # 130%91 39
    if r==0:
        break
    else:
        divident = divisor
        divisor = r

print(divisor)