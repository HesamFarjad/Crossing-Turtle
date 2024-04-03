from turtle import Turtle, Screen
from player import Player
import time
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = Cars()
scoreboard = Scoreboard()

game_on = True
while game_on:

    time.sleep(0.1)
    screen.update()
    screen.title("Cross Turtle")

    # Player move
    screen.listen()
    screen.onkey(key="Up", fun=player.move_up)

    # Win case of player
    if player.ycor() > 280:
        scoreboard.level_up()
        player.start_point()
        cars.speed_up()

    # Random car generate
    cars.generate_car()
    cars.move_car()

    # Lose case of player
    for i in cars.all_cars:
        if i.distance(player) < 20:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()
