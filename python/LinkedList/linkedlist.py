class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

    def __repr__(self) -> str:
        repr = str(self.val) + "->"
        while self.next:
            repr += str(self.next.val) + "->"
            self.next = self.next.next
        return repr

    def deleteNode(self, node) -> None:
        node.val = node.next.val
        node.next = node.next.next

    def createNextNode(self, node) -> None:
        self.next = node

if __name__ == "__main__":
    node = ListNode(0)
    linked_list = node
    for i in range(1, 10):
        node.next = ListNode(i)
        node = node.next
    print(linked_list)