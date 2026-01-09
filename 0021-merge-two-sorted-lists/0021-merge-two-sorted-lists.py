class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        l3 = ListNode()
        node = l3
        while node:
            if node1 and node2 and node1.val > node2.val:
                node.next = node2
                node2 = node2.next
            elif node1:
                node.next = node1
                node1 = node1.next
            elif node2:
                node.next = node2
                node2 = node2.next
            node = node.next
        return l3.next