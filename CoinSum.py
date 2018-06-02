def getValI(i):
	if (i)>0:
		return result[i]
	else:
		return 0
n = int(input())
s = list(map(int, input().split()))
result = [0 for i in range(n+1)]
for x in s:
	result[x] += 1
for i in range(1, n+1):
	result[i] += sum([getValI(i-p) for p in s])
print(result)