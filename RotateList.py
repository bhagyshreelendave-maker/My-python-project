class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Count nodes
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Make circular list
        tail.next = head

        # Reduce k
        k = k % length

        # Find new tail
        steps = length - k
        newTail = head
        for i in range(steps - 1):
            newTail = newTail.next

        # New head
        newHead = newTail.next
        newTail.next = None

        return newHead
