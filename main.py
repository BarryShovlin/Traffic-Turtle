
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Traffic Turtle")
player = Player()
car_manager = CarManager()
screen.onkey(player.move_up, "Up")
scoreboard = Scoreboard()
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.reset_turtle()
        car_manager.level_up()

screen.exitonclick()