// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(original,cloned,target):
            if not original or not cloned:
                return
            
            if original==target:
                return cloned
            
            return dfs(original.right,cloned.right,target) or dfs(original.left,cloned.left,target)
        
        return dfs(original,cloned,target)
        