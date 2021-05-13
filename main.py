x = [2,3,8,1,0,-3,-12,123,22,91,111,-35,-5]

def bubble_sort (arr):
	for a in arr:
		for b in range(len(arr) - 1):
			if arr[b] > arr[b + 1]:
				arr[b], arr[b + 1] = arr[b + 1], arr[b]
	return arr

print(bubble_sort(x))