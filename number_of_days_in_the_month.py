'''
You will be provided with a number. Print the number of days in the month corresponding to that number.

Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

Input Description:
The input is in the form of a number.

Output Description:
Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

Sample Input :
8
Sample Output :
31
'''
a = int(input())
months30 = [4,6,9,11]
if a>12 or a<1:
    print('Error')
elif a==2:
    print(28)
elif a not in months30:
    print(31)
else:
    print(30)