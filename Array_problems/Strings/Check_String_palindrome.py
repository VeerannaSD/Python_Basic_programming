'''
 Radha newly learnt about palindromic strings.A palindromic string is a string which is same when read from left to right and also from right to left.Help her in implementing the logic.

 

Input Description:
You are given a String āsā

Output Description:
Print 1 if String is palindrome or 0 if not

Sample Input :
NITIN
Sample Output :
1
'''
s=input()
reverseS=s[::-1]
if s==reverseS:
    print(1)
    
else:
    print(0)