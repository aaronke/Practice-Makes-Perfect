# [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/)

## Description
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

## Analysis
### Clarifications
1. What's the requirements for the complexity? No

### Methods
**Method 1 --** Convert the iterator into a list. Therefore, we can access the last element by constant time.

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

**Method 2 --** Use `self.Peek` and `self.hasPeek` to store the most front element on the stack. And then each time, it will return the peek value at constant time. And every time executing `next` method, peek value and status will be updated.

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Python Code

~~~
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

# class PeekingIterator(object):
#     def __init__(self, iterator):
#         """
#         Initialize your data structure here.
#         :type iterator: Iterator
#         """
#         self.nums = []
#         while iterator.hasNext():
#             self.nums.append(iterator.next())
#         # self.nums =  list(reversed(self.nums))
#         self.nums.reverse()

#     def peek(self):
#         """
#         Returns the next element in the iteration without advancing the iterator.
#         :rtype: int
#         """
#         if self.hasNext():
#             return self.nums[-1]
        

#     def next(self):
#         """
#         :rtype: int
#         """
#         if self.hasNext():
#             return self.nums.pop()
        

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return True if len(self.nums) > 0 else False
        
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.hasPeek = False
        if self.iterator.hasNext():
            self.Peek = self.iterator.next()
            self.hasPeek = True
            
        
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasPeek:
            return self.Peek
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasPeek:
            temp = self.Peek
            self.hasPeek = False
            if self.iterator.hasNext():
                self.hasPeek = True
                self.Peek = self.iterator.next()
            return temp
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iterator.hasNext() or self.hasPeek
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
~~~
