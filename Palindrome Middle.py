class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Solution:
    def isPalindrome(self, head):
        """
Reverse function being created
        """
        def reverse(head):
            # will have to understand the whole function
            prev = None #prev None
            while head is not None:
                next = head.next #next is head next
                head.next = prev # head next = None
                prev = head # prev = head
                head = next # overall operation ta ekhono bujtesi na
            return prev

        if head is None or head.next is None:
            return True

        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        head_second_half = reverse(slow)
        copy_head_second_half = head_second_half

        while head is not None and head_second_half is not None:
            if head.val != head_second_half.val:
                break

        reverse(copy_head_second_half)

        if head is None or head_second_half is None:
            return True

        return False




