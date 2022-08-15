'''
Write a code get an integer number as input and print the sum of the digits.

Input Description:
A single line containing an integer.

Output Description:
Print the sum of the digits of the integer.

Sample Input :
124
Sample Output :
7
'''

N = int(input())
sum = 0
while N:
    q = N//10
    r = N%10
    sum+=r
    N=q
print(sum)