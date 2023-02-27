#end of Session Upload.

#Weekly Repositories.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def FindMiddle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.value

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(29)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Middle Pointer: " + str(FindMiddle(head)))

main()
