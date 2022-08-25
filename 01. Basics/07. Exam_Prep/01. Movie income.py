movie = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_percent = int(input())

one_day_income = tickets * ticket_price
whole_period_income = one_day_income * days
clean_income = whole_period_income - (whole_period_income * cinema_percent/100)

print(f"The profit from the movie {movie} is {clean_income:.2f} lv.")
