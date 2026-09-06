class Solution:
    def pairAndSum(self, arr):
        # code here
        # Basic nested loop apporach. Fails on time
        # total = 0
        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)):
        #         total += arr[i]&arr[j]
        # return total
        total = 0
        n = len(arr)
        for bit in range(31):  # Assuming 32-bit integers
            mask = 1 << bit
            count = 0
            for num in arr:
                if num & mask:
                    count += 1
            total += (count * (count - 1) // 2) * mask
        return total
        
        
        