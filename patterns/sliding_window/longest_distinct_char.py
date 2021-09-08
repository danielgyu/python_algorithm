def solution(word: str, n: int) -> str:
    cur_string, max_string = "", ""
    char_set = set()

    for c in word:
        char_set.add(c)

        if (len(char_set) > n) and (len(max_string) < len(cur_string)):
            char_set.pop()
            max_string = cur_string
            cur_string = ""

        elif len(char_set) > n:
            char_set.pop()
            cur_string = ""

        else:
            cur_string += c

    return max_string if max_string else cur_string


def solution_length(word: str, n: int) -> int:
    window_start = 0
    max_length = 0
    word_dict = {}

    for window_end in range(len(word)):
        if word[window_end] not in word_dict:
            word_dict[word[window_end]] = 0
        word_dict[word[window_end]] += 1

        while len(word_dict) > n:
            word_dict[word[window_start]] -= 1
            if word_dict[word[window_start]] == 0:
                del word_dict[word[window_start]]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
        

print(solution("araaci", 2))
print(solution("araaci", 1))
print(solution("cbbebi", 3))
print(solution("cbbebi", 10))
print(solution_length("araaci", 2))
print(solution_length("araaci", 1))
print(solution_length("cbbebi", 3))
print(solution_length("cbbebi", 10))
