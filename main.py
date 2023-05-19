import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=turtle.move_forward)

count = 0
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    if count == 6:  # Using 6 to generate cars, else the screen is logged with too many cars.
        # So for every 6 times, car will be created.
        car_manager.create_car()
        count = 0

    for car in car_manager.cars:
        car.forward(car_manager.car_speed)  # Move cars
        if car.distance(turtle) < 20:  # Detecting collision
            game_is_on = False
            score = Scoreboard()
            score.print_game_over()

    # Check if turtle has reached the finish line
    if turtle.check_finish_line():
        score.level += 1
        turtle.reset_position()
        score.print_level()
        car_manager.increase_speed() # After level increase, increase speed of cars.

    screen.update()
    count += 1

screen.exitonclick()
