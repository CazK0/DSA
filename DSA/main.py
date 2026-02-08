from src.sliding_window import max_profit, length_of_longest_substring, character_replacement
from src.two_pointers import is_palindrome, two_sum_sorted, three_sum
from src.fast_slow import ListNode, has_cycle, middle_node, detect_cycle


def create_linked_list(arr, pos=-1):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    nodes = [head]

    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        curr.next = node
        curr = node
        nodes.append(node)

    if pos != -1:
        curr.next = nodes[pos]

    return head


def run_sliding_window():
    print("--- SLIDING WINDOW ---")
    print(f"Stock Profit: {max_profit([7, 1, 5, 3, 6, 4])}")
    print(f"Longest Substring: {length_of_longest_substring('abcabcbb')}")
    print(f"Char Replacement: {character_replacement('AABABBA', 1)}\n")


def run_two_pointers():
    print("--- TWO POINTERS ---")
    print(f"Is Palindrome: {is_palindrome('A man, a plan, a canal: Panama')}")
    print(f"Two Sum: {two_sum_sorted([2, 7, 11, 15], 9)}")
    print(f"3Sum: {three_sum([-1, 0, 1, 2, -1, -4])}\n")


def run_fast_slow():
    print("--- FAST & SLOW POINTERS ---")

    l1 = create_linked_list([1, 2, 3, 4, 5])
    mid = middle_node(l1)
    print(f"Middle of [1..5]: {mid.val if mid else 'None'}")

    l2 = create_linked_list([3, 2, 0, -4], 1)
    print(f"Has Cycle: {has_cycle(l2)}")

    start_node = detect_cycle(l2)
    print(f"Cycle Start Value: {start_node.val if start_node else 'None'}\n")


if __name__ == "__main__":
    run_sliding_window()
    run_two_pointers()
    run_fast_slow()
