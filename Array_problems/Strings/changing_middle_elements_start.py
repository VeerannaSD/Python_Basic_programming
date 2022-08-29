'''
Given a string S, print it after changing the middle element to * (if the length of the string is even, change the 2 middle elements to *).
Sample Testcase :
INPUT
hello
OUTPUT
he*lo
'''

s=input()
if len(s)%2==0:
    result = s[0:int(len(s)/2)-1]+'**'+s[int(len(s)/2)+1:]
    # ='*'
    # result=s.replace(s[len(s)/2-1], "*")
    # ='*'
else:
    result = s.replace(s[int(len(s)/2)], "*")
print(result)