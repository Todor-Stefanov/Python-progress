n = int(input())

# negative_list = []
# positive_list = []

positive_list = list()
negative_list = list()

# positive_counter = 0
negative_sum = 0
for i in range(n):
    nums = int(input())
    if nums >= 0:
        # positive_counter += 1
        positive_list.append(nums)
    else:
        negative_sum += nums
        negative_list.append(nums)
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {negative_sum}")
