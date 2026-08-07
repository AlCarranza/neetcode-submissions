# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Save reference for head
        dummy = ListNode(0,head)

        # Find the position of left
        before = dummy
        for _ in range(left-1):
            before = before.next

        # 'tail' is the first node of the sublist.
        # After reversing, it becomes the tail.
        tail = before.next

        prev = None
        curr = tail
        
        # Reverse the sublist
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Re arrange: tail should point to the end of the sublist
        #             before should point to the new head of the sublist
        tail.next = curr
        before.next = prev

        return dummy.next
            
        
