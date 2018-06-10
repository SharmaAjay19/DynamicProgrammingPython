class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        nback = head
        nbackprev = head
        curr = head
        while n>0:
            curr = curr.next
            n += -1
        while curr:
            curr = curr.next
            nbackprev = nback
            nback = nback.next
        if nback == head:
            return nback.next
        else:
            nbackprev.next = nback.next
            nback.next = None
            return head