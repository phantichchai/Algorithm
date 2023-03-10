import random

# Structure of list node  
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 382. Linked List Random Node

class Random:
    # When declare this class will store the value of linklist to extra space 'range'
    # Time complexity: O(n)
    # Space complexity: O(n)    
    def __init__(self, head: ListNode):
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next
    
    # random number from range list
    # Time complexity: O(1)
    # Space complexity: O(1)    
    def getRandom(self) -> int:
        return random.choice(self.range)

if __name__ == '__main__':
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    
    obj = Random(node1)
    for i in range(5):
        print(obj.getRandom())
