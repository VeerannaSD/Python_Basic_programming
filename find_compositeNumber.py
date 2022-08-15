'''
Given a number N, print 'yes' if it is composite else print 'no'.
Sample Testcase :
INPUT
123
OUTPUT
yes
'''
n=int(input())
a=[]
count1=0
if n==0 or n==1:
    print('no')
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
    else:
        continue
#print(f'Number of factors for {n} is:',len(a))
#print(f'Factors for {n} are:',a)
if(len(a)>2):
    print('yes')
else:
    print('no')