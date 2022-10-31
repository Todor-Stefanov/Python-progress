numbers = list(map(int, input().split(" ")))
target_number = int(input())

iteration_counter = 0
unique_dict = {}
for i in range(len(numbers)):
    for g in range(i+1, len(numbers)):
        if numbers[i] + numbers[g] == target_number:
            print(f"{numbers[i]} + {numbers[g]} = {target_number}")
            if (numbers[i], numbers[g]) not in unique_dict.items():
                unique_dict[numbers[i]] = numbers[g]

        iteration_counter += 1
print(f"Iterations done: {iteration_counter}")
[print(f"({key}, {value})") for key, value in unique_dict.items()]