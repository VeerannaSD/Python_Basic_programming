'''
Find the first 0 in window of size k. You  are given n numbers and window size ‘w’

Your task is to print the first index which has 0

Input Description:
You are given two numbers ‘n’ and ‘w’ n representing size of array and ‘w’ size of window

Output Description:
Print the index of first 0(1 basedindexing),if there is no index with 0 print -1

Sample Input :
7 2
1 0 6 7 4 0 9
Sample Output :
2 2 -1 -1 6 6
'''
a,b =input().split()
inta=int(a)
intb=int(b)
c =list(map(int,input().split()))
zero_index=[]
for i in range(0,len(c)-intb+1):
   # print(c[i:i+intb])
    if 0 in c[i:i+intb]:
       # print('hi')
        for j in range(i,i+intb):
            #print(j)
            if c[j] == 0:
                #print('index',j+1)
                zero_index.append(j+1)
                break
    else:
        zero_index.append(-1)
print(*zero_index)