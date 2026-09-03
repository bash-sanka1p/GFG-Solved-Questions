class Solution:
    def maxDiffSum(self, arr):
        # code here
        keep = 0
        one = 0

        for i in range(1, len(arr)):
            new_keep = max(
                keep + abs(arr[i] - arr[i - 1]),
                one + abs(arr[i] - 1)
            )

            new_one = max(
                keep + abs(1 - arr[i - 1]),
                one + abs(1 - 1)
            )

            keep = new_keep
            one = new_one

        return max(keep, one)