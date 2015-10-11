# 面经 -- http://www.1point3acres.com/bbs/thread-143930-1-1.html
# 找两个字符串中长度为N以上的共同子串
class Solution(object):	
	def shareSubString(self, n, s1, s2):
		subString = self.getSubString(n, s1)
		rs = []
		for sub in subString:
			if sub in s2:
				rs.append(sub)
		return rs

	def  getSubString(self, n, s):
		l = len(s)
		subs = []
		if n+1 > l:
			return subs
		for i in xrange(n+1, l+1):
			start = 0
			end = i
			while end < l+1:
				if s[start:end] not in subs:
					subs.append(s[start:end])
				start += 1
				end += 1
		return subs

s = Solution()

s1 = "abcd"
s2 = "abcdc"
n = 1

print s.shareSubString(n, s1, s2)
# Test Cases
# s1 = "abd"
# s2 = "abdc"
# n = 1
# Complexity -- Time -- O(n^(n-k)  Space -- O(n^(n-k) 

