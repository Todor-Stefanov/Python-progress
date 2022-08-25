book_pages = int(input())
pages_hour = int(input())
days = int(input())
one_booktime = book_pages // pages_hour
hours_needed = one_booktime // days
print(hours_needed)


#from math import floor
#number_of_pages_of_current_book = int(input())
#read_pages_per_hour = int(input())
#number_of_days = int(input())

#overall_time = floor(number_of_pages_of_current_book / read_pages_per_hour)
#needed_hours = overall_time / number_of_days

#print(f"{needed_hours:.0f}")