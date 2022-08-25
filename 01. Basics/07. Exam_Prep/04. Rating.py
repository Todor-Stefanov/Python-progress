import sys
movie_number = int(input())
min_rating = sys.maxsize
max_rating = -sys.maxsize
movie_rating_couter = 0
top_rated_movie = ""
least_rated_movie = ""
for _ in range(movie_number):
    movie_name = input()
    movie_rating = float(input())
    if movie_rating >= max_rating:
        max_rating = movie_rating
        top_rated_movie = movie_name
    elif movie_rating < min_rating:
        min_rating = movie_rating
        least_rated_movie = movie_name
    movie_rating_couter += movie_rating

averege_movie_rating = movie_rating_couter / movie_number

print(f"{top_rated_movie} is with highest rating: {max_rating:.1f}")
print(f"{least_rated_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {averege_movie_rating:.1f}")



