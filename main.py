import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager(screenWidth=screen.window_width(), screenHeight=screen.window_height() - 100)

screen.onkey(key="Up", fun=player.move_up)
scoreboard = Scoreboard()
game_is_on = True
# speed = 0.1
while game_is_on:
    # print(f"speed:{speed}")
    time.sleep(0.1)
    screen.update()
    scoreboard.refresh()
    car_manager.refresh()

    # check is player crash with car
    if (car_manager.is_crash(player)):
        scoreboard.game_over()
        game_is_on = False

    # check player position
    if player.is_at_finish_line():
        player.go_to_start()
    # if player.ycor() > FINISH_LINE_Y:
    #     player.goto(STARTING_POSITION)
        scoreboard.add_level()
        car_manager.level_up()
        # speed *= 0.9

screen.exitonclick()
