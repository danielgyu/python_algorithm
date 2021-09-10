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
            count_dict[window_end] = 1
            window_start += 1
            max_length = max(max_length, cur_length)
            cur_length = 1

    return max_length if max_length else cur_length


if __name__ == "__main__":
    print(solution("abcabcbb"))
    print(solution("bbbbb"))
    print(solution("pwwkew"))
    print(solution(""))
