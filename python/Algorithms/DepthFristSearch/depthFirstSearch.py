class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class RangeSumBST:
    def iterative(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if high > node.val:
                    stack.append(node.right)
        return ans
    
    def recursive(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            nonlocal ans
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    dfs(node.left)
                if high > node.val:
                    dfs(node.right)
        ans = 0
        dfs(root)
        return ans 

class MaxPathSum:
    def recursive(self, root: Optional[TreeNode]) -> int:
        # initialize in minimum result that to lowest value
        self.res = float("-inf")

        # define depth-first search that traversal on tree
        def dfs(node):
            # check if node is not node return zero value
            if not node:
                return 0

            # recurse for find max sum of the left sub-tree node
            left_max = dfs(node.left)
            # recurse for find max sum of the right sub-tree node
            right_max = dfs(node.right)

            # find max sum of the single path between value of current node with current plus with max of left or right node
            max_single_path = max(node.val, node.val + max(left_max, right_max))
            # update max sum of the maximum sum of this tree by current result, max single path (max from plus just left or right node)
            # and current node with left and right node
            self.res = max(self.res, max_single_path, node.val + left_max + right_max)

            return max_single_path
        
        dfs(root)
        return self.res