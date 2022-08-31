def odd_even_sum(num_str: str):
    list_string = list()
    for i in num_str:
        i = int(i)
        list_string.append(i)
    sum_of_even = 0
    sum_of_odd = 0
    for j in list_string:
        if j % 2 == 0:
            sum_of_even += j
        else:
            sum_of_odd += j
    print(f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}")


numbers = input()
odd_even_sum(numbers)
