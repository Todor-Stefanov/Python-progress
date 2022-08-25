pens = int(input()) * 5.80
markeri = int(input()) * 7.20
chem = int(input()) * 1.20
discount = int(input()) / 100

all_sum = pens + markeri + chem
real_sum = all_sum - (all_sum * discount)
print(real_sum)

#pen_price = 5.80
#highlighter_price = 7.20
#detergent_per_liter = 1.20

#number_of_pens = int(input())
#number_of_highlighters = int(input())
#liters_of_detergent = int(input())
#discount_percentage = int(input()) / 100

#pens_price = pen_price * number_of_pens
#highlighters_price = highlighter_price * number_of_highlighters
#detergent_price = detergent_per_liter * liters_of_detergent

#sum_without_discount = pens_price + highlighters_price + detergent_price
#overall_sum = sum_without_discount - (sum_without_discount * discount_percentage)

#print(overall_sum)