ACTION = 0
ID = 1
NAME = 2

def make_mapper(records: list) -> dict:
    mapper = {}
    for r in records:
        split = r.split(" ")
        if r.startswith("E") and split[ID] not in mapper:
            mapper[split[ID]] = split[NAME]
        elif r.startswith("C"):
            print(split)
            mapper[split[ID]] = split[NAME]
        else:
            continue

    return mapper


def solution(records: list) -> list:
    res = []

    mapper = make_mapper(records) 
    print(mapper)

    for r in records:
        split = r.split(" ")
        if r.startswith("E"):
            res.append(f"{mapper[split[1]]}님이 들어왔습니다.")
        elif r.startswith("L"):
            res.append(f"{mapper[split[1]]}님이 나갔습니다.")

    return res

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
