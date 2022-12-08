class LeafSimilar:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf1, leaf2 = iterative(root1), iterate(root2)
        
        # check the number of node are equal if not then return False
        if len(leaf1) != len(leaf2):
            return False

        # iterate through both list and check all node are equal
        for l1, l2 in zip(leaf1, leaf2):
            # if not then return False
            if l1.val != l2.val:
                return False
        # after finish the loop show that the two given binary trees are leaf-similar also I return True
        return True

def iterative(root):
    # traversal to both binay tree with depth first search
    # iterate untill the stack is empty
    stack, leafs = [root], []
    while stack:
        # pop the top of stack to the current node   
        node = stack.pop()

        # if the node are leaf then add this node to the list 'leaf'
        if not (node.left or node.right):
            leafs.append(node)

        # if the node has right node then add right node to the stack
        if node.right:
            stack.append(node.right)

        # if the node has left node then add left node to the stack
        if node.left:
            stack.append(node.left)
    return leafs