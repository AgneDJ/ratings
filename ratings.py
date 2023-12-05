"""Restaurant rating lister."""


# put your code here
def rating(filename):
    restaurant = input("What is your restaurant?")
    rating = input()

    opened = open(filename, "a")
    file = opened.write(restaurant)
    file = opened.write(rating)

    ratings = {}

    for line in file:
        line = line.rstrip()
        items = line.split(':')
        first_item = items[0]
        second_item = int(items[1])

        ratings[first_item] = second_item
        something = ratings.items()

    type(something)
    something = sorted(something)
    print(something)


filename = "scores.txt"
rating(filename)
