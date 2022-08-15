'''
Let P represent Paper, R represent Rock and S represent Scissors. Given 2 out of the 3 determine which one wins. If its a draw print 'D'.
Sample Testcase :
INPUT
R P
OUTPUT
P
'''

#Rock vs Paper->Paper wins 
#Rock vs Scissors->Rock wins 
#Paper vs Scissors->Scissors wins 
a =list(input().split())
if (a[0]=='R' and a[1]=='P') or (a[0]=='P' and a[1]=='R'):
    print('P')
elif (a[0]=='R' and a[1]=='S') or (a[0]=='S' and a[1]=='R'):
    print('R')
elif (a[0]=='P' and a[1]=='S') or (a[0]=='S' and a[1]=='P'):
    print('S')
else:
    print('D')