from typing import List

def max_profit(prices: List[int]) -> int:
    l, r = 0, 1
    max_p = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
        else:
            l = r
        r += 1
    return max_p

def length_of_longest_substring(s: str) -> int:
    char_map = {}
    l = 0
    res = 0
    for r in range(len(s)):
        if s[r] in char_map:
            l = max(char_map[s[r]] + 1, l)
        char_map[s[r]] = r
        res = max(res, r - l + 1)
    return res

def character_replacement(s: str, k: int) -> int:
    count = {}
    res = 0
    l = 0
    max_f = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_f = max(max_f, count[s[r]])
        while (r - l + 1) - max_f > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res