class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def middle_node(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def detect_cycle(head: ListNode) -> ListNode:
    slow = head
    fast = head
    is_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            is_cycle = True
            break
    if not is_cycle:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow