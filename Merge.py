class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the starting point
        dummy = ListNode()
        current = dummy
        
        # 2. Iterate while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # 3. If one list is longer, attach the remainder
        current.next = list1 if list1 else list2
        
        # Return the actual start of the merged list
        return dummy.next
