class Solution(object):
    d= {0: "Zero", 1:"One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10 : "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
    level = ['Thousand', 'Million', 'Billion']
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 20:
            return self.d[num]
        result = []
        numberList = []
        while (num):
            numberList.append(num % 10)
            num = num/10
        l =  len(numberList)
        if l == 2:
            return ' '.join(self.twoDigit(numberList))
        nextLevel = -1
        while l - 3 >=0 :
            threeDigitRs = self.threeDigit(numberList[0:3]) # Normal Two Digits
            if nextLevel >= 0 and threeDigitRs:
                threeDigitRs += [self.level[nextLevel]]

            result = threeDigitRs + result   
            numberList = numberList[3:]
            nextLevel += 1
            l = len(numberList)

        if l == 1:
            result = [self.d[numberList[0]],self.level[nextLevel]] + result
        if l == 2:
            result = self.twoDigit(numberList[0:2]) + [self.level[nextLevel]] + result
            
        return ' '.join(result)
        
    def threeDigit(self, threeDigit):
        rs = []
        if threeDigit[2] != 0:
            rs = [self.d[threeDigit[2]], "Hundred"]
        rs = rs + self.twoDigit(threeDigit[0:2])
        return rs

    def twoDigit(self, twoDigit):
        number = 10*twoDigit[1] + twoDigit[0]
        if number == 0:
            return []
        if number in self.d:
            return [self.d[number]]
        return [self.d[twoDigit[1] * 10], self.d[twoDigit[0]]]
        
s = Solution()

# print s.numberToWords(1234567)        
print s.numberToWords(100)   
# print s.numberToWords(1000000)   
# print s.numberToWords(123)
# print s.numberToWords(10)