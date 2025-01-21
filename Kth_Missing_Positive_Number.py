class Solution:
    def findKthPositive(self, arr, k):
        n = len(arr)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            missing = (arr[mid] - (mid + 1))
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return low + k

# Main function for user input and function call
solution = Solution()
# Get array and k as input
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
k = int(input("Enter the value of k: "))

result = solution.findKthPositive(arr, k)
print("The kth positive missing number is:", result)

