from src.sliding_window import max_profit, length_of_longest_substring, character_replacement
from src.sliding_window import max_profit, length_of_longest_substring, character_replacement
from src.two_pointers import is_palindrome, two_sum_sorted, three_sum

def run_tests():
    print("--- Stock Profit ---")
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {prices} -> Max Profit: {max_profit(prices)}")

    print("\n--- Longest Substring ---")
    s = "abcabcbb"
    print(f"String: {s} -> Length: {length_of_longest_substring(s)}")

    print("\n--- Character Replacement ---")
    s2 = "AABABBA"
    k = 1
    print(f"String: {s2}, k={k} -> Max Length: {character_replacement(s2, k)}")
if __name__ == "__main__":
    run_tests()

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

if __name__ == "__main__":
    run_sliding_window()
    run_two_pointers()
