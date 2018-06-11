class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        node1 = head
        node2 = node1.next
        if node2:
            head = node2
            head.next = node1
        tempnode = node2.next
        while node1 and node2:
            node1.next = tempnode
            node2.next = node1
            node1 = tempnode
            if node1:
                node2 = node1.next
            if node2:
                tempnode = node2.next
        return head
            