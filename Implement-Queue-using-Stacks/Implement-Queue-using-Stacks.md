#[Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
## Descriptions
Implement the following operations of a queue using stacks.

* push(x) -- Push element x to the back of queue.
* pop() -- Removes the element from in front of queue.
* peek() -- Get the front element.
* empty() -- Return whether the queue is empty.

**Notes:**
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.  
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.  
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

## Analysis
At the beginning, I misunderstood the easy issue that using list to represent stack. However the thing is that I need to use stack to represent queue. However, in python, there is not stack structure, basically it is list. So I think it is fine to use the list to represent the idea `First in, First out`(while for stack, it is `Last in, First Out`.

But there are more correct way to do it. See the note [link](http://bookshadow.com/weblog/2015/07/07/leetcode-implement-queue-using-stacks/). To be Updated!

## Python
~~~
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.numList = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.numList.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.numList.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.numList[0]
        
    def empty(self):
        """
        :rtype: bool
        """
        if self.numList:
            return False
        return True   # beat 35%
        # return False if self.numList else True --beat 0.22%
~~~
## Notes
1. There are another details in implementation. When I check the empty of list, there are two kinds of code. See following. Why does method 2 is so bad?

~~~
# Method 1 -- beat 35%
if self.numList:
    return False
return True   
# Method 3 -- beat 0.22%
# return False if self.numList else True 
~~~