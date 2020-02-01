#fortune teller using functions and loops

#variables
colors = ["red", "yellow", "green"]
numbers = ["13", "24", "42", "555"]
fortunes = [["You will find a pretty flower", "You will find a lucky penny", "You will meet a cute puppy"],
            ["You will get free ice cream today", "You will have no bugs in your code", "You will see a cool bird today"],
            ["You will reach new heights", "You will accomplish great things", "You will find a new yummy dish"],
            ["You will find a new favorite ingredient", "You will find a wonderful book", "You will encounter little traffic today"]]

#function(s)
#determine if the entered item by the user is in the list. if not, end the program. if the item exists, determine its index in the list.
#use the index values as coordinates to determine the fortune to print
def fortune_teller(x, y):
    for item in colors:
        if (colors.count(x) == 0):
            exit
        else:
            colors_coordinate = int(colors.index(x))
    for item in numbers:
        if (numbers.count(y) == 0):
            exit
        else:
            numbers_coordinate = int(numbers.index(y))
    print(fortunes[numbers_coordinate][colors_coordinate])

#fortune telling - program for user interaction.
    #user_color is the color selected by the user when prompted
    #user_number is the number selected by the user when prompted
user_color = input("Pick a color: red, yellow, and green.\nWrite it here: ")
user_number = input("Pick a number: 13, 24, 42, 555.\nWrite it here: ")

fortune_teller(user_color, user_number)