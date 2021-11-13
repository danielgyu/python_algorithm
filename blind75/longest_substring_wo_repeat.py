def longest_substring(s: str) -> int:
    longest, window_left = 0, 0
    current = str()
    i = 0

    while window_left < len(s):

        while (i < len(s)) and (s[i] not in current):
            current += s[i]
            i += 1
        
        longest = max(longest, len(current))

        current = s[window_left]
        window_left += 1
        i = window_left

    return longest

if __name__ == "__main__":
    print(longest_substring("dvdf"))
    print(longest_substring("abcabcbb"))
    print(longest_substring("bbbb"))
    print(longest_substring("pwwkew"))
    print(longest_substring("kkddddjabcd"))
