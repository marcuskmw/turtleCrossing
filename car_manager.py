import random
from turtle import Turtle
import math

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    refresh_counter = 0

    def __init__(self, screenWidth, screenHeight):
        self.all_cars = []
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.speed = STARTING_MOVE_DISTANCE

    def get_new_car(self):
        car = Turtle()
        car.turtlesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.goto(self.screenWidth / 2, random.randrange(-self.screenHeight / 2, self.screenHeight / 2))
        return car

    def refresh(self):
        # add a car for every 5 refresh
        if self.refresh_counter % 6 == 0:
            self.all_cars.append(self.get_new_car())

        for car in self.all_cars:
            if car.xcor() <= - self.screenWidth / 2:
                self.all_cars.remove(car)
                car.hideturtle()
                del car
            else:
                car.goto(car.xcor() - self.speed, car.ycor())

        self.refresh_counter += 1

    def is_crash(self, player):
        for car in self.all_cars:
            # if abs(car.ycor() - player.ycor()) < 10:
            #     # car and player at the same level
            #     if 0 < car.xcor() - player.xcor() < 20:
            #         return True
            if player.distance(car)<=20:
                return True

        return False

    def level_up(self):
        self.speed+=MOVE_INCREMENT