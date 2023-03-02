from turtle import *
import random

screen=Screen()
game_on=True
screen.title("!!!!Welcome to the turtle race game!!!!!")
screen.setup(width=500,height=400)
y_position=[-70,-40,-10,20,50,80]
col=["red","blue","green","cyan","black","pink"]
turtle_list = []
set = True

while game_on:
    for t in range(0,6):
        tim = Turtle(shape="turtle")
        tim.color(col[t])
        tim.penup()
        tim.goto(x=-240,y=y_position[t])
        turtle_list.append(tim)
    while set:
        guess=screen.textinput("Make a guess", "Enter color of turtle who will win? ")
        if guess not in col:
            set=True
        else:
            set=False

    if guess:
        is_on = True

    while is_on:

        for turtle in turtle_list:
            if turtle.xcor() > 240:
                is_on=False
                winning_color=turtle.pencolor()
                if winning_color == guess:
                    r=Turtle()
                    r.hideturtle()
                    r.write(f"You have won !!!!",font=("algebrian",10,"bold"),align='center')
                else:
                    r=Turtle()
                    r.hideturtle()
                    r.write(f"You have lost !!!! , {winning_color} turtle have won it",font=("algebrian",10,"bold"),align='center')
            turtle.forward(random.randint(0,10))
        
    gam=screen.textinput("want_to_play_again?","Enter yes or no: ")
    if gam=="yes":
        game_on=True
    else:
        game_on=False

screen.exitonclick()