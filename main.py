x = [2,3,8,1,0,-3,-12,123,22,91,111,-35,-5]

def f (arr):
	for i in arr:
		for j in range(len(arr) - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr

print(f(x))
