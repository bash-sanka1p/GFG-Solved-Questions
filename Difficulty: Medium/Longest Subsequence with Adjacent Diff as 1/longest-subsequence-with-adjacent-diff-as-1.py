class Solution:
    def longestSubseq(self, arr):
        n = len(arr)

        # Base case: if the array has only one element
        if n == 1:
            return 1

        # Dictionary to store the length of the 
        # longest subsequence
        dp = {}
        ans = 1

        for i in range(n):

            # Check if the current element is adjacent to 
            # another subsequence
            if arr[i] + 1 in dp or arr[i] - 1 in dp:
                dp[arr[i]] = 1 + max(dp.get(arr[i] + 1, 0), \
                                     dp.get(arr[i] - 1, 0))
            else:
                dp[arr[i]] = 1

            # Update the result with the maximum
            # subsequence length
            ans = max(ans, dp[arr[i]])
            
        return ans