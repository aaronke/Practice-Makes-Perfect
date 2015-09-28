# [Rectangle Area](https://leetcode.com/problems/rectangle-area/)

## Description
Find the total area covered by two rectilinear rectangles in a 2D plane. Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

**Rectangle Area:** Assume that the total area is never beyond the maximum possible value of int.
## Analysis
### Clarifications
1. It return the total area not overlapping area!!
2. The area could be 0, correct?

### Method
Get the area of both rectangle and then deduct the overlap part.

* Time Complexity: `O(1)`
* Space Complexity: `O(1)`

## Python Code
~~~
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """              
        :type A: int
        :type B: int
        :type C: intd
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        #AE CG
        width = 0
        # if E > C or A > G :
        #     width = 0
        if  A <= E and E <= C:
            width = min(C,G) - E
        elif  E <= A and A <= G:
            width = min(G,C) - A
        
        # CD GH
        height = 0
        # if H <= B or D < F :
        #     height = 0
        if  B <= F and F <= D:
            height = min(D,H) - F
        elif  F <= B and B <= H:
            height = min(H,D) - B
        
        overlap = height*width
        
        area1 = (C-A)*(D-B) 
        area2 = (G-E)*(H-F)
        
        return area1+area2-overlap
~~~
## Test Cases
~~~
A,B,C,D,E,F,G,H
0,0,0,0,-1,-1,1,1 -> 4
-2,-2,2,2,-2,-2,2,2 -> 8
~~~
****