class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def countTreeNodes(node) -> int:
    if node == None:
        return 0
    return (1 + countTreeNodes(node.left) + countTreeNodes(node.right))

def maxDepth(node) -> int:
    if node == None:
        return 0
    return 1 + max(maxDepth(node.left), maxDepth(node.right))

if __name__ == '__main__':
    node = TreeNode(0)
    node.left = TreeNode(1)
    node.right = TreeNode(2)
    print(f'count = {countTreeNodes(node)}')
    print(f'depth = {maxDepth(node)}')