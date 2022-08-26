import math
centuries = int(input())
century_to_year = 100 * centuries
year_to_days = math.floor(365.2422 * century_to_year)
days_to_hours = 24 * year_to_days
hours_to_minutes = days_to_hours * 60

print(f"{centuries} centuries = {century_to_year} years = {year_to_days} days = {days_to_hours} hours = {hours_to_minutes} minutes")
