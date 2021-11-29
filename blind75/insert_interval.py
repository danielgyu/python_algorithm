def insert_interval(intervals: list, new_interval: list) -> list:

    if new_interval[0] > intervals[-1][1]:
        return intervals + [new_interval]

    elif new_interval[1] < intervals[0][0]:
        return [new_interval] + intervals

    i = 0
    res = []
    while i < len(intervals):

        if new_interval[1] < intervals[i][0]:
            res.append(new_interval)
            res.append(intervals[i])

        elif new_interval[0] > intervals[i][1]:
            res.append(intervals[i])
        
        elif (new_interval[0] >= intervals[i][0] and
              new_interval[1] > intervals[i][1]):

            interval = [intervals[i][0]]

            while new_interval[1] > intervals[i][1]:
                i += 1

            if new_interval[1] >= intervals[i][0]:
                interval.append(intervals[i][1])
                res.append(interval)
            else:
                interval.append(new_interval[1])
                res.append(interval)
                res.append(intervals[i])

        else:
            res.append(intervals[i])

        i += 1

    return res


if __name__ == "__main__":
    print(insert_interval([[1, 3], [6, 9]], [2, 5]))
    print(insert_interval([[1, 2],[3, 5],[6, 7],[8, 10],[12, 16]], [4, 8]))
    print(insert_interval([[3, 5]], [1, 2]))
    print(insert_interval([[1, 2], [3, 4]], [5, 6]))
    # TODO this doesn't work
    print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
