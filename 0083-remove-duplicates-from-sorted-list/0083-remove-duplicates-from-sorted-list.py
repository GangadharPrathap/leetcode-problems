
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        prev = head
        curr = head.next
        while curr:
            if prev.val != curr.val:
                prev = curr
                curr = curr.next
            else:
                while prev.val == curr.val:
                    curr = curr.next
                    if not curr:
                        prev.next = None
                        break
                prev.next = curr
        return head