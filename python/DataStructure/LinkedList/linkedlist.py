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

def oddEvenList(head: ListNode) -> ListNode:
        # if the linked list is empty list then return 'None'
        if not head:
            return None

        # Create pointers for point to odd, even, and temporal start even node
        # by start_even point to the head node.next
        start_even = head.next
        # by odd point to the head node
        odd = head
        # by even point to the start_even pointer
        even = start_even

        # iterate until odd node and even node is none
        while odd.next and even.next:
            # move pointer odd next node to odd next of next node
            odd.next = odd.next.next
            # change current odd node to the odd next node
            odd = odd.next
            # move pointer even next node to even next of next node
            even.next = even.next.next
            # change current even node to the even next node
            even = even.next
        
        # link the last odd node next with start_even pointer
        odd.next = start_even
        # return head of linked list
        return head  

if __name__ == "__main__":
    node = ListNode(0)
    linked_list = node
    for i in range(1, 10):
        node.next = ListNode(i)
        node = node.next
    print(f"Original linked list: {representList(linked_list)}")
    print(f"Mid node of this linked list is: {middleNode(linked_list).val}")
    print(f"Odd Even List is: {representList(oddEvenList(linked_list))}")
