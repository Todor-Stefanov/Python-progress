n = int(input())

# ===

positive = list()
negative = list()
even = list()
odd = list()

for i in range(n):
    nums = int(input())
    if nums % 2 == 0:
        even.append(nums)
    else:
        odd.append(nums)
    if nums >= 0:
        positive.append(nums)
    else:
        negative. append(nums)

filter_word = input()

print(eval(filter_word))


#if filter_word == "even":
 #   print(even)
#if filter_word == "odd":
 #   print(odd)
#if filter_word == "positive":
 #   print(positive)
#if filter_word == "negative":
 # print(negative)


# filtered_list = list()

# for current_number in numbers_list:
    # if filter_word == "even":
        # if current_number % 2 == 0:
            # filtered_list.append(current_number)
    # if filter_word == "odd":
        # if current_number % 2 != 0:
            # iltered_list.append(current_number)
    # if filter_word == "positive":
        # if current_number >= 0:
            # filtered_list.append(current_number)
    # if filter_word == "negative":
        # if current_number <= 0:
            # filtered_list.append(current_number)


#print(filtered_list)