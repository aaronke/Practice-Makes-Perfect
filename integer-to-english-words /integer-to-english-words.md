
# [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

## Description
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than `2^31 - 1`. For example,

~~~
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
~~~

## Analysis
At the beginning, I wrongly thought each module is divided by 2 digits. But the truth is that each module should be divided by 3 digits. And with 3 digits, we share the same method.

Another difficulty is to distingwish the situations: `1)`, `2)` and `3)` could be discussed specifically. But for the result we could apply generlized method (Deal with 3 digit per loop). 

~~~
1) 0
2) 1 ~ 9
3) 10 ~ 20
4) 21 ~ 999
5) 1000 ~999999 
.....
~~~

Finally, as for displaying result, originally, I used one string to represent all the middle results. However, it would a mess to controll the space when combining middle results. Therefore, a better way to do it is to take advantage of array in python. 

There must be better methods. I will do research about them in future.

## Python Code
~~~
class Solution(object):
    digits = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
    decades = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    level = ['Thousand', 'Million', 'Billion']
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        if num <= 9:
            return self.digits[num - 1]
        result = []
        numberList = []
        while (num):
            numberList.append(num % 10)
            num = num/10
        l =  len(numberList)
        if l == 2:
            return ' '.join(self.twoDigit(numberList))
        nextLevel = -1  # Apply level after 3 digits
        while l - 3 >=0 :
            threeDigitRs = self.threeDigit(numberList[0:3]) # Normal Two Digits
            if nextLevel >= 0 and threeDigitRs:
                threeDigitRs += [self.level[nextLevel]]

            result = threeDigitRs + result   
            numberList = numberList[3:]
            nextLevel += 1
            l = len(numberList)
        
        if l == 1:
            result = [self.digits[numberList[0] - 1],self.level[nextLevel]] + result
        if l == 2:
            result = self.twoDigit(numberList[0:2]) + [self.level[nextLevel]] + result
            
        return ' '.join(result)
        
    def threeDigit(self, threeDigit):
        rs = []
        if threeDigit[2] != 0:
            rs = [self.digits[threeDigit[2] - 1], "Hundred"]
        print self.twoDigit(threeDigit[0:2])
        rs = rs + self.twoDigit(threeDigit[0:2])
        return rs

    def twoDigit(self, twoDigit):
        if twoDigit[0] == 0 and twoDigit[1] == 0:
            return []
        if twoDigit[0] != 0 and twoDigit[1] == 0:
            return [self.digits[twoDigit[0] - 1]]       
        if twoDigit[1] == 1:
            return [self.digits[10 + twoDigit[0] - 1]]
        if twoDigit[1] >= 2 and twoDigit[0] >= 1:
            return [self.decades[twoDigit[1] - 2], self.digits[twoDigit[0] - 1]]
        if twoDigit[1] >= 2 and twoDigit[0] == 0:
            return [self.decades[twoDigit[1] - 2]]
~~~

## Notes
1. Apply correct data struction:
When it comes to get `'Thousand', 'Million', 'Billion'`, firstly I tried used a stupid method.

		# hundred = 'Hundred'
		# h = 100
		# thousand = 'Thousand'
		# t = 1000
		# million = 'Million'
		# m = 1000000
		# billion = 'Billion'
		# b = 1000000000  
		
	A better way to do it -- Just use index to get value
`level = ['Thousand', 'Million', 'Billion']`

2. How to use class varible in python.  
StackOverflow [Link](http://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function)  
The basic idea is shown in code above. Define varible in class but outside of functions. And if using in function, add `self.` before the variable name.

3. How to join string in array
   Stackoverflow [Link](http://stackoverflow.com/questions/493819/python-join-why-is-it-string-joinlist-instead-of-list-joinstring)  
    Just apply `' '.join(targetList)` as example code above.

4. At the beginning, I made tons of mistakes about creating modules. Understand relationship FIRSTLY!
 

 