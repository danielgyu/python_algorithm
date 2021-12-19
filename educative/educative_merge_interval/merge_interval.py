def merge(intervals):
    res = []
    sorted_intervals = sorted(intervals)
    start, end = sorted_intervals[0][0], sorted_intervals[0][1]

    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] > end:
            res.append([start, end]) 

            start = sorted_intervals[i][0]
            end = sorted_intervals[i][1]

        elif sorted_intervals[i][1] > end:
            end = sorted_intervals[i][1]

    res.append([start, end])

    return res


if __name__ == "__main__":
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge([[1, 4], [4, 5]]))
