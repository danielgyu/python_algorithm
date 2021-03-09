# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0

    for i, ch in enumerate(s):
        if (ch in used) and (start <= used[ch]):
            start = used[ch] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used[ch] = i

    return max_length

s = "pwwkew"
print(lengthOfLongestSubstring(s))