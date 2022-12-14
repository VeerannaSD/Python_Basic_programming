'''
You are a passport issuer, but due to some problems in the system, there are redundant  passport numbers. Your task is to delete all the duplicate passport numbers. You are given a list of passport numbers.

Input Description:
You are given length of list.Second line,You are given with a list.

Output Description:
Print the list of passport numbers without duplicates.

Sample Input :
5
A23 B56 B56 C79 D16
Sample Output :
A23 B56 C79 D16
'''

n = int(input ())
redundent_passport = list(map(str,input().split()))
passport = list(dict.fromkeys(redundent_passport))
print(*passport)