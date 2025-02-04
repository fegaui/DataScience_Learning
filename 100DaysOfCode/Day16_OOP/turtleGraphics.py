# from turtle import Turtle, Screen
# fel = Turtle() ### Classes usually start with with UpperCase
# fel.shape("turtle")
# fel.color("brown1", "firebrick2")
# fel.forward(230)
# print(fel)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)



