'''
You are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest.

Print the output up to two decimal places (Round-off if necessary).

(S.I. = P*T*R/100)

Input Description:
Three values are given to you as the input. these values correspond to Principle amount, Interest Rate and Time in that particular order.

Output Description:
Find the Simple interest and print it up to two decimal places. Round off if required.

Sample Input :
1000 2 5
Sample Output :
100.00
'''
a = input()
b = list(a.split(" "))
p = float(b[0])
t = float(b[1])
r = float(b[2])
#si = round(p*t*r/100,2)
#112.20
print("{:0.2f}".format(p*t*r/100))