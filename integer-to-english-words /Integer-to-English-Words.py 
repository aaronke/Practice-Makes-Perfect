class Solution(object):
    digits = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
    decades = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    level = ['Thousand', 'Million', 'Billion']
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # hundred = 'Hundred'
        # h = 100
        # thousand = 'Thousand'
        # t = 1000
        # million = 'Million'
        # m = 1000000
        # billion = 'Billion'
        # b = 1000000000
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

        
        
s = Solution()

# print s.numberToWords(1234567)        
# print s.numberToWords(12345)   
# print s.numberToWords(1000000)   
# print s.numberToWords(123)
# print s.numberToWords(10)
