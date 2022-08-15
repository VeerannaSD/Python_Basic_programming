'''

You are given with an circular array .Your task is calculate the difference between two consecutive number. And if difference is greater than ‘k’, print 1 else print 0

Input Description:
You are given two numbers ‘n’, ’m’. Next line contains n space separated integers.

Output Description:
Print 1 if the difference is greater than ‘m’.

Sample Input :
5 15
50 65 85 98 35
Sample Output :
0 1 0 1 0
'''
a,b = input().split()
inta = int(a)
intb = int(b)
c = list(map(int,input().split()))
d = []
for i in range(len(c)-1):
    if c[i] - c[i+1] > intb or c[i+1]-c[i]>intb:
        d.append(1)
    else:
        d.append(0)
if c[0] - c[len(c)-1]>intb or c[len(c)-1]-c[0]>b:
    d.append(1)
else:
    d.append(0)
print(*d)