'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''
        
class Solution:
    def absDiff(self, root):
        # code here
        inord = []
    
        # inorder of BST gives sorted values
        inorder(inord, root)
    
        mini = float('inf')
        n = len(inord)
    
        # since array is sorted, just check adjacent elements
        for i in range(n - 1):
            mini = min(mini, inord[i + 1] - inord[i])
    
        return mini
    
# simple inorder traversal to store values
def inorder(inord, root):
    if root is None:
        return

    inorder(inord, root.left)
    inord.append(root.data)
    inorder(inord, root.right)
