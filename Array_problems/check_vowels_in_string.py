'''
Given a string S, print 'yes' if it has a vowel in it else print 'no'.
Sample Testcase :
INPUT
codekata
OUTPUT
yes
'''
a=input()
flag=False
for i in a:
    if i in ['a','e','i','o','u']:
        flag=True
        break
    else:
        continue
if flag:
    print('yes')
else:
    
    print('no')