from collections import deque

class Solution:
    def getCount(self, root, k):

        if root is None:
            return 0

        q = deque()
        q.append((root, 1))

        leaf_costs = []

        while q:
            curr, level = q.popleft()

            # If current node is a leaf
            if curr.left is None and curr.right is None:
                leaf_costs.append(level)
                continue

            if curr.left is not None:
                q.append((curr.left, level + 1))

            if curr.right is not None:
                q.append((curr.right, level + 1))

        # Visit cheapest leaves first
        leaf_costs.sort()

        count = 0

        for cost in leaf_costs:
            if cost > k:
                break

            k -= cost
            count += 1

        return count