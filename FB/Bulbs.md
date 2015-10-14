# [Bulbs](https://codelab.interviewbit.com/problems/bulbs/)

## Description
N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb. Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs. You can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.

Example:

~~~
Input : [0 1 0 1]
Return : 4

Explanation :
	press switch 0 : [1 0 1 0]
	press switch 1 : [1 1 0 1]
	press switch 2 : [1 1 1 0]
	press switch 3 : [1 1 1 1]
~~~
## Analysis
At the beginning, my solution is generally following the definition of the program. Every time it gets `0`, it will reset the status of bulbs in the right of current bulbs. However, the time complexity is too much.

* Time Complexity: `O(n^2)`
* Space Complexity: `O(1)`

But afterwards, I found if the status is stored by integer, it must have more power to store additional status. What we interests is just about the true of false (`1` or `0`). Therefore, I think of making switch times at status list. It can save some variables and simplify the code. However, it still needs `O(n^2)` time.

Both methods above are solve the issues, but they have low efficiency. After that, I think of other ways to get ride of the for loop for updating status after one switch. Finally, I found just use A values plus times and then did mode!! That's all you need to get new status!!  

## Python Code
~~~
class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
    	 # Method 1
        # times = 0 
        # for i in xrange(len(A)):
        #     if A[i] == 0:
        #         times += 1
        #         A[i] = 1
        #         allTrue = True
        #         for j in range(i+1, len(A)):
        #             if A[j] == 0:
        #                 A[j] = 1
        #             else:
        #                 A[j] = 0
        #                 allTrue = False
        #         if allTrue:
        #             return times
        # return 0
        
        # Refined Method 2
        # times = 0 
        # for i in xrange(len(A)):
        #     if A[i]%2 == 0:
        #         times += 1
        #         for j in range(i, len(A)):
        #             A[j] += 1

        # return times     

		 # Refined Method 3
        times = 0 
        for i in xrange(len(A)):
            if (A[i] + times)%2 == 0:
                times += 1

        return times     
~~~
## Test Cases
~~~
1. [1,1,1,1,0] -> 1
2. [1,1,1,1,1] -> 0
3. [1,1,1,0,0] -> 1
4. [1,0,1,0] -> 4
5. [0,1,1,1] -> 2
~~~

## FB Solution
The order in which you press the switch does not affect the final state.

Example:

~~~
Input : [0 1 0 1]

Case 1:
Press switch 0 : [1 0 1 0]
Press switch 1 : [1 1 0 1]

Case 2:
Press switch 1 : [0 0 1 0]
Press switch 0 : [1 1 0 1]	
~~~

Therefore we can choose a particular order. To make things easier lets go from left to right. At the current position if the bulb is on we move to the right, else we switch it on. This works because changing any switch to the right of it will not affect it anymore.
~~


C++ solution offered by FB:

~~~
class Solution {
    public:
	    int bulbs(vector<int> &A) {
		    int state= 0, ans = 0;
		    for (int i = 0;i < A.size();i++) {
			    if (A[i] == state) {
				    ans++;
				    state = 1 - state;
			    }
		    }
		    return ans;
	    }
};
~~~


