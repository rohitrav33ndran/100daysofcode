import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_list = []


screen.listen()
screen.onkey(player.up,"Up")

game_is_on = True
count = 0
car_speed = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1 # Track the iterations

    #Create cars every 6 iterations
    if count % 6 == 0:
        car_manager = CarManager()
        car_list.append(car_manager)

    #For each car in car list check if the player distance is less than 20 pixels. This detects collision
    for car in car_list:
        #if to check game over and move cars only if not. This freezes the car movement once the game is over
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
        else:
            car.move(car_speed)

    #check if the player reached next level and if yes then increase car speed and score
    if player.ycor() > player.FINISH_LINE_Y:
        car_speed += 1
        scoreboard.level_up()
        player.refresh()
        for car in car_list:
            car.move(car_speed)


screen.exitonclick()