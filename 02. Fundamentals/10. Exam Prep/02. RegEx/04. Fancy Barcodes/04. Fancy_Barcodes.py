import re

n = int(input())

regex_string = r"\@#+([A-Z][A-Za-z0-9]{4,}[A-Z])\@#+"
regex_nums = r"[0-9]"
for i in range(n):
    text = input()

    matches_barcodes = re.findall(regex_string, text)

    if not matches_barcodes:
        print("Invalid barcode")
        continue


    matches_nums = re.findall(regex_nums, matches_barcodes[0])

    if len(matches_nums) == 0:
        print("Product group: 00")

    else:
        product_group = ""
        for num in matches_nums:
            product_group += num
        print(f"Product group: {product_group}")
