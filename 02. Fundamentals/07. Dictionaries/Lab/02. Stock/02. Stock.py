in_stock = input().split(" ")
request = input().split(" ")
in_stock_dict = {}

for i in range(0, len(in_stock), 2):
    key = in_stock[i]
    value = in_stock[i + 1]
    in_stock_dict[key] = int(value)

for i in range(len(request)):
    if request[i] in in_stock_dict.keys():
        print(f"We have {in_stock_dict[request[i]]} of {request[i]} left")
    else:
        print(f"Sorry, we don't have {request[i]}")
