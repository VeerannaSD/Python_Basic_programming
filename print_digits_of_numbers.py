'''
Write a code to get an integer N and print the digits of the integer.

Input Description:
A single line contains an integer N.

Output Description:
Print the digits of the integer in a single line separated by space,

Sample Input :
348
Sample Output :
3 4 8

'''

N = int(input())
rem = 1
digits= []
test = N
while test:
    r = test//10
    rem = test%10
    digits.append(rem)
    test = r
print(*digits[::-1])
    
    