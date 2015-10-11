# [GCD](https://codelab.interviewbit.com/problems/gcd/)

## Description
Given 2 non negative integers `m` and `n`, find `gcd(m, n)`

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both `m` and `n` fit in a 32 bit signed integer.

Example

~~~
m : 6
n : 9
~~~
GCD(m, n) : 3   
**NOTE :** DO NOT USE LIBRARY FUNCTIONS
## Analysis
### Clarifications
1. How do you deal with when there is one input whose value is zero? Get the maximum of input!

### Method
**Naive Method**  Get all the divisors(sorted) for input `m` firstly. And then Find the maximum number among the list that is also the divisor of `n`.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

**Use idea of deduction -- Dynamic Programming** Based on the feature of GCD, the GCD of `m` and `n` is the same as the GCD of `(m-n, m)` or `(n-m, n)`. At the beginning, I used recursions to solve it, but it is too deep and costs too much.

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

**Hint:**  
Lets say g is gcd(m, n) and m > n.

~~~
m = g * m1
n = g * m2
m - n = g * (m1 - m2)
gcd (m, n) = gcd(m-n, n)
~~~



## Python Code
~~~
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    # def gcd(self, A, B):
    #     if A == 0 or B == 0:
    #         return max(A, B)
    #     count = 1
    #     rs = [1]
    #     while count < A:
    #         count += 1
    #         if A%count == 0:
    #             rs.append(count)
    #     while rs:
    #         v = rs.pop()
    #         if B%v == 0:
    #             return v
    def gcd(self, A, B):
        if A == 0 or B == 0:
            return max(A, B)
        if A == B:
            return A
            
        while A != B:
            if A > B:
                A = A-B
            elif A < B:
                B = B-A
            if A == B:
                return A
~~~

## Test Cases

~~~
1. 2,2  -> 2
2. 6, 9 -> 3
3. 1, 13 -> 1
4. 4, 6 -> 2
~~~

## Suggested Solutions From FB

### Explanation
~~~
Lets say g is gcd(m, n) and m > n.

m = g * m1
n = g * m2

m - n = g * (m1 - m2)

gcd (m, n) = gcd(m-n, n)

           = gcd(m - 2n, n) if m >= 2n
           = gcd(m - 3n, n) if m >= 3n 
             .
             .
             .
           = gcd(m - k*n, n) if m >= k*n
           
       In other words, we keep subtracting n till the result is greater than 0. Ultimately we will end up with m % n.
       
              So gcd(m, n)  = gcd(m % n, n) 
~~~

### Code

~~~
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, a, b):
        if (b == 0):
		    return a
        else:
		    return self.gcd(b, a%b)
~~~