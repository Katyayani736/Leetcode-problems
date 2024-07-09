class Solution:
    def averageWaitingTime(self, customers) -> float:
        ct = 0
        wt = 0
        for at, bt in customers:
            ct = max(ct,at) + bt
            wt += ct - at
        return wt / len(customers)

customers = [[1, 2], [2, 5], [4, 3]]

solution = Solution()
average_waiting_time = solution.averageWaitingTime(customers)
print(f"Average waiting time: {average_waiting_time:.2f}")
