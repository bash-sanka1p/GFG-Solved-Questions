class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        n = len(arr)

        # Sort the first half in ascending order
        arr[:n//2] = sorted(arr[:n//2])

        # Sort the second half in ascending order
        arr[n//2:] = sorted(arr[n//2:])

        count = 0
        right = n // 2

        # Iterate through the first half of the array
        for left in range(n // 2):

            # Move right pointer while dominance condition holds
            while right < n and arr[left] >= 5 * arr[right]:
                right += 1

            # Count dominant pairs
            count += (right - n // 2)

        return count
