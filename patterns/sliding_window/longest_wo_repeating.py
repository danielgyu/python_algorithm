# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def solution(s: str) -> int:
    window_start = 0
    cur_length, max_length = 0, 0
    count_dict = {}
    
    for window_end in s:
        if not count_dict.get(window_end):
            count_dict[window_end] = 1
            cur_length += 1
            
        elif count_dict.get(window_end) == 0:
            count_dict[window_end] += 1
            cur_length += 1
            
        else:
            max_length = max(max_length, cur_length)
            while s[window_start] != window_end:
                count_dict[s[window_start]] = 0
                window_start += 1
                cur_length -= 1
            window_start += 1
            count_dict[window_end] = 1

    return max(max_length, cur_length)


if __name__ == "__main__":
    """
    """
    assert solution("abcabcbb") == 3
    assert solution("bbbb") == 1
    assert solution("pwwkew") == 3
    assert solution("aab") == 2
    assert solution("") == 0
    assert solution("dvdf") == 3
    assert solution("cdd") == 2
    assert solution("tmmzuxt") == 5
    assert solution("aabaab!bb") == 3
