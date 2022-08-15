'''
Given 2 numbers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1
Sample Testcase :
INPUT
10 5
OUTPUT
5
'''

def gcd(a, b):
  # Find minimum of a and b
  result = min(a, b)
   
  while result:
    if a % result == 0 and b % result == 0:
      break
    result -= 1
   
  # Return the gcd of a and b
  return result
lista=list(map(int,input().split()))
a = abs(lista[0])
b = abs(lista[1])

if(gcd(a, b)):
    print(gcd(a, b))
else:
    print(-1)