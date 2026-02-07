from typing import List


def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1

    while l < r:
        cur_sum = numbers[l] + numbers[r]
        if cur_sum > target:
            r -= 1
        elif cur_sum < target:
            l += 1
        else:
            return [l + 1, r + 1]
    return []

def three_sum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res