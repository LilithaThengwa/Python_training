movies = [

    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},

    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},

    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},

    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},

    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},

]

#Task 1

# titles = list(map(lambda movie: movie["title"], movies))

# print(titles)

#===================================================================

# Task 1.1 - Find average for all - map, filter, all, ...

# Dont use for loop or List comp

# ave_rating = list(map(lambda x: sum(x["ratings"]) / len(x["ratings"]), movies))
# print(ave_rating) 

#==========================================================

# Task 1.2 - Find average for all - map, filter, all, ...

# movie_average = list(map(lambda movie: {**movie, "average_rating": sum(movie["ratings"]) / len(movie["ratings"])}, movies))

# print(movie_average)

#==========================================================

# Task 2

movie_average = list(map(lambda x: {**x, "average_rating": sum(x["ratings"]) / len(x["ratings"])}, movies))

# top_rated = max(movie_average, key=lambda x: x["average_rating"])
# print(f"The top rated movie is {top_rated['title']}. ")

#==========================================================

# Task 3

high_ave = list(filter(lambda x: x["average_rating"] >= 4.6, movie_average))

sorted_titles3 = list(map(lambda x: x["title"], high_ave))

# print(sorted_titles3)

#==========================================================

#task 4

sorted_movies = sorted(movie_average, key = lambda x: x["average_rating"], reverse = True)

sorted_titles4 = list(map(lambda x: x["title"], sorted_movies))

print(sorted_titles)
