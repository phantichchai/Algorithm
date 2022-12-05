class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

    def deleteNode(self, node) -> None:
        node.val = node.next.val
        node.next = node.next.next

    def createNextNode(self, node) -> None:
        self.next = node

def representList(head: ListNode) -> str:
        repr = ""
        while head:
            repr += str(head.val) + "->"
            head = head.next
        return repr

def middleNode(head: ListNode) -> ListNode:
        # create two pointer that point to head slow and fast
        slow, fast = head, head
        # iterate until fast and fast.next not equal None mean the list has no more next node
        while fast and fast.next:
            # update current slow by move one step each time
            slow = slow.next
            # update current fast by move two steps each time
            fast = fast.next.next
            
        # return current slow which is a middle node
        return slow    

if __name__ == "__main__":
    node = ListNode(0)
    linked_list = node
    for i in range(1, 10):
        node.next = ListNode(i)
        node = node.next
    print(representList(linked_list))
    print(f"Mid node of this linked list is {middleNode(linked_list).val}")
