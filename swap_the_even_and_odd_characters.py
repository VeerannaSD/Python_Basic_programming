'''
Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).
Input Size : |s| <= 10000000(complexity O(n))
Sample Testcase :
INPUT
codekata
OUTPUT
ocedakat

'''

S = input()
listS = list(S)
#print(listS)
newS=[]
for i in range(0,len(listS),2):
    if i+1>len(listS):
        break
    else:
        a,b=listS[i+1],listS[i]
        newS.append(a)
        newS.append(b)
#print(newS)
newSS = ''
for i in newS:
 #   print(i)
    newSS=newSS+i
print(newSS)
