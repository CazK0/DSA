from src.sliding_window import max_profit, length_of_longest_substring, character_replacement

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