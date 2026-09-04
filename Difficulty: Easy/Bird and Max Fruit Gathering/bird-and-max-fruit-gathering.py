class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        """ code here """
        # Array apporach
        # max_fruits = 0
        # arr.extend(arr[:m])
        
        # for i in range(len(arr)-m):
        #     # print(i, i+m)
        #     max_fruits = max(max_fruits, sum(arr[i:i+m]))
        # return max_fruits
        
        
        # Sliding Window Approach
        max_fruits = 0
        arr.extend(arr[:m])
        
        s = sum(arr[:m])
        max_fruits = s
        for i in range(m,len(arr)):
            # print(i-m, i)
            s -= arr[i-m]
            s += arr[i]
            
            max_fruits = max(s, max_fruits)
        
        return max_fruits
            