def searchIndex(A):
	l = len(A)
	if l == 0:
		return -1
	if l == 1:
		return [0]

	left = 0
	curI = 0
	right = sum(A[1:])
	rs = []
	while curI < l:
		if left == right:
			rs.append(curI)

		left += A[curI]
		if curI == l-1:
			right = 0
		else:
			right -=  A[curI + 1]
		curI += 1

	return rs

print searchIndex([-1])
print searchIndex([1,1,-1])
print searchIndex([-1,1,1,1,-1])
print searchIndex([3,-3,1])
print searchIndex([3,-3,2,3,4,1,-9])

