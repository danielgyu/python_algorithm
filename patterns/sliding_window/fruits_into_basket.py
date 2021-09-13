def solution(fruits: list) -> int:
    window_start = 0 
    max_length = 0
    fruit_counter = {}

    for window_end in range(len(fruits)):
        fruit = fruits[window_end]

        if fruit_counter.get(fruit) is None:
            fruit_counter[fruit] = 1
        elif fruit_counter.get(fruit):
            fruit_counter[fruit] += 1

        max_length = max(max_length, sum(fruit_counter.values()))
 
        while len(fruit_counter) > 2:
            starting_fruit = fruits[window_start]
            
            fruit_counter[starting_fruit] -= 1
            if fruit_counter[starting_fruit] == 0:
                del fruit_counter[starting_fruit]

            window_start +=1

    return max_length


fruits = ['A', 'B', 'C', 'A', 'C']
print(solution(fruits))
assert solution(fruits) == 3
fruits = ['A' , 'B', 'C', 'B', 'B', 'C']
print(solution(fruits))
assert solution(fruits) == 5

