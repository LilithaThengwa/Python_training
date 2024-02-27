import re

# quote = "To be or note to be"

# # r - raw string
# # without raw string would need to escape all the time.
# is_be = re.search(r"be$", quote)
# output = "Present and end with be" if is_be else "Not present"
# # search returns none if there are no matches, or a re.Match object if there are. Stops after first match.

# print(is_be, type(is_be))
# print(output)

# quote1 = "funny funy funnny fuzzy"
# find_be = re.findall(r'fu[nz]{2}y', quote1)
# print(find_be)

# return all matches as a list of strings.

#================================================

tweet = "Spoiler: This movie is great, but the spoiler was unexpected. Avoid sharing spoilers!"

censor_tweet = re.sub(r"(spoiler|but)", "*" * 7, tweet, flags=re.IGNORECASE)

# print(censor_tweet)

#================================================

list_websites = "facebook.com, google.com, yahoo.com, amazon.com, twitter.in"

# result = re.sub(r"(\w+).com", "blackist.com", list_websites)
# result = re.sub(r"(.*).com", "blackist.com", list_websites)
result = re.sub(r"(\w+)(\.com)", r"\1.subdomain\2", list_websites)
# print(result)

#================================================

names = ["  John Doe  ", "  Jane   Smith", "Alice Johnson  ", "Chris Evans"]


output = [re.sub(r'\s*(\w+)\s+(\w+)\s*',r'\2, \1', name) for name in names]
print(output)

#================================================

# post = "Loving the #sunny weather in #California. #travel #fun"

# output = re.findall(r'#\w+', post)

# print(output)