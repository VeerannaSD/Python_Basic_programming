'''

You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.

Input Description:
First line contains a number ānā. Then next line contains n space separated numbers.

Output Description:
Print the difference of indices of largest and smallest array

Sample Input :
5
1 6 4 0 3
Sample Output :
-2
'''

n = int(input())
a = list(map(int, input().split(' ')))
#print(a)
x = max(a)
#print(x)
y = min(a)
#print(y)

#print(f'Index of {x} and {y}')
#print(a.index(x))
#rint(a.index(x))
#rint(a.index(x))
#print(a.index(y))
res = a.index(x) - a.index(y)
print (res)