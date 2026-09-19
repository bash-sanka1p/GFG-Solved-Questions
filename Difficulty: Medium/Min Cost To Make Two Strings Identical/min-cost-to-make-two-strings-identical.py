class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        # code here
        # Ensure the shorter string determines the DP array size.
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            costS1, costS2 = costS2, costS1

        n, m = len(s1), len(s2)
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])

            # Reuse the current row as the previous row for the next iteration.
            prev, curr = curr, prev

        lcsLength = prev[m]

        return ((n - lcsLength) * costS1 +
                (m - lcsLength) * costS2)
