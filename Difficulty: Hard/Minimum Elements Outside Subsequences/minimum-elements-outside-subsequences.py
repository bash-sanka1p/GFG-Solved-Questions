class Solution:
    def minCount(self, arr):
        """ code here """
        
        n = len(arr)

        dp = [[[0] * (n + 1) for _ in range(n + 1)]
              for _ in range(n + 1)]

        for idx in range(n - 1, -1, -1):

            for incLast in range(-1, n):

                for decLast in range(-1, n):

                    ans = 1 + dp[idx + 1][incLast + 1][decLast + 1]

                    if incLast == -1 or arr[idx] > arr[incLast]:
                        ans = min(ans,
                                  dp[idx + 1][idx + 1][decLast + 1])

                    if decLast == -1 or arr[idx] < arr[decLast]:
                        ans = min(ans,
                                  dp[idx + 1][incLast + 1][idx + 1])

                    dp[idx][incLast + 1][decLast + 1] = ans

        return dp[0][0][0]