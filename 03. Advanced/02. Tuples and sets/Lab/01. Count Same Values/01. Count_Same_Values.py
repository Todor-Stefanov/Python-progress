numbers = tuple(map(float, input().split(" ")))  # -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
nums_and_occurances = {}
for num in numbers:  # num = -2.5
    if num not in nums_and_occurances:
        nums_and_occurances[num] = 0  # стойността на ключа = 0 {-2.5:0}
    nums_and_occurances[num] += 1  # отброява честотата на срещанията


[print(f"{key} - {value} times") for key, value in nums_and_occurances.items()]  # цикъл, който да принтира стойностите на ключовете, вкарани в nums_and_occurances

