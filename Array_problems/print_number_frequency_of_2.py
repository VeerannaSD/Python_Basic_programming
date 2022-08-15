'''
You are provided with an array in which all elements are repeated thrice except one which is repeated twice.Your task is to print that number.

 

O(n) time and O(1) extra space

Input Description:
First line contains a number denoting size of array ‘n’.Next line contains n space separated numbers

Output Description:
Print the number which is repeated twice

Sample Input :
5
13 12 13 12 13
Sample Output :
12
'''
n = int(input())
a = list(map(int,input().split()))
for i in a:
    if a.count(i)==2:
        print(i)
        break
    
