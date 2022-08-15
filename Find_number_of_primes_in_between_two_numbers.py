'''
Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).
Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)
Sample Testcase :
INPUT
2 5
OUTPUT
3
'''

def isPrime(num):
    for i in range(2,num):#2,5
        if num%i==0:
            return False
    return True
a=list(map(int,input().split()))
primes=[]
for i in range(a[0],a[1]+1):#2,5
    if a[0]==0 or a[1]==1 or a[0]==1 or a[1]==1:
        break
    elif i==2:
        primes.append(i)
        continue
    else:
        if(isPrime(i)):#4
            primes.append(i)
#print(primes)
print(len(primes))