class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if not head:
            return head
        node1 = head
        node2 = node1.next
        if not node2:
            return head
        tempnode = self.swapPairs(node2.next)
        node1.next = tempnode
        node2.next = node1
        return node2

def printList(headL):
    resl = []
    curr = headL
    while curr:
        resl.append(curr.val)
        curr = curr.next
    print(resl)

def createList(nList):
    head = ListNode(nList[0])
    curr = head
    for x in nList[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    return head

sol = Solution()
inp = list(map(int, input().split(",")))
lst = createList(inp)
printList(sol.swapPairs(lst))