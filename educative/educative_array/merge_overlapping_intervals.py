from dataclasses import dataclass


@dataclass
class Pair:
    x: int
    y: int


def solution(l: list) -> list:
    answer = [Pair(l[0].x, l[0].y)]

    for i in range(1, len(l)):
        if l[i].x > answer[-1].x and l[i].x > answer[-1].y:
            answer.append(l[i]) 
        elif l[i].y > answer[-1].y:
            answer[-1].y = l[i].y

    return answer


if __name__ == "__main__":
    v1 = [Pair(1, 5), Pair(4, 8), Pair(11, 15)]
    v2 = [Pair(1, 5), Pair(3, 7), Pair(4, 6), 
         Pair(6, 8), Pair(10, 12), Pair(11, 15)]

    print(solution(v1))
    print(solution(v2))
