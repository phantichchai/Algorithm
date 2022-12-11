class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # initialize value of the maximum difference equal to the minimum posible result
        self.result = 0

        # define the dfs for traversal through binary search that habe three parameters
        # node define at the current node that to compute new result
        # current_max is a maximum value of this sub-tree
        # current_min is a min value of this sub-tree
        def dfs(node, current_max, current_min):
            # if node are not the TreeNode then end of recurse
            if not node:
                return 
            # compute the result by find a maximum amount 'current result', absolute value of current_max and current node value
            # and absolute value of curent_min and current node value
            self.result = max(self.result, abs(current_max - node.val), abs(current_min - node.val))

            # compare new value of current maximum
            current_max = max(current_max, node.val)
            # compare new value of current min
            current_min = min(current_min, node.val)

            # do recurse to the left sub-tree node
            dfs(node.left, current_max, current_min)
            # do recurse to the right sub-tree node
            dfs(node.right, current_max, current_min)

        # start the depth-first-search through binary tree
        dfs(root, root.val, root.val)

        # then return the result
        return self.result