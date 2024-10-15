def binarySearch(inputArr, target):
	# returns -1 if element not found, or index of target if found
	# Time Complexity: O(log(N))
	# Space Complexity: O(1)
	if (len(inputArr) == 0):
		return -1

	left = 0
	right = len(inputArr) - 1

	while left <= right:
		middle = (left+right)//2
		if inputArr[middle] == target:
			return middle

		if inputArr[middle] < target:
			left = middle + 1
		elif inputArr[middle] > target: # this can also be just an else, and the above if an elif, but since we are returning if inputArr[middle] == target, I prefer this for clarity
			right = middle - 1
	return -1

def main():
	arr1 = [1, 3, 5, 6, 7, 8, 9, 13, 15, 20, 29, 30, 31, 33, 35, 36]
	testValues = [36, 1, 35, 3, 20, 15, 88, -100, 0]
	
	for val in testValues:
		search1Res = binarySearch(arr1, val)
		print(f"Searching arr1 for {val}, index of target: {'Not found (-1)' if search1Res == -1 else search1Res}")

if __name__ == "__main__":
	main()