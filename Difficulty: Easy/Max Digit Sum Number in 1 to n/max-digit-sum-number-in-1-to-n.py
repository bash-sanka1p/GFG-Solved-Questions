class Solution:
    def digitSum(self, x):
        total = 0
    
        while x > 0:
            total += x % 10
            x //= 10
    
        return total
    
    
    def findMax(self,n):
        ans = n
        maxSum = self.digitSum(n)
    
        # x is used to process the digits of n from right to left
        x = n
    
        # b represents the place value of the current digit
        b = 1
    
        while x > 0:
    
            # Decrease the current digit by 1 and
            # replace all digits to its right with 9.
            #
            # Example:
            # x = 52, b = 10
            # (52 - 1) * 10 + 9 = 519
            cur = (x - 1) * b + (b - 1)
    
            # Calculate the digit sum of the generated candidate
            total = self.digitSum(cur)
    
            # Update the answer if:
            # 1. Current candidate has a larger digit sum, or
            # 2. Digit sums are equal but current candidate is larger
            if total > maxSum or (total == maxSum and cur > ans):
                maxSum = total
                ans = cur
    
            # Remove the current digit and move to the next digit
            x //= 10
    
            # Move to the next place value
            b *= 10
            
        return ans