from turtle import Screen
from cannon import Cannon
from alien import Alien, AlienShot
from laser import Laser
from bunker import Bunker
from scoreboard import Scoreboard, Lives
import random

# Create Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Space Invaders")
screen.tracer(0)

# Create cannon
cannon = Cannon((0, -250))
# Create laser beam
laser = Laser()
# Create Alien shot
alien_shot = AlienShot()
# Craete Scoreboard
scoreboard = Scoreboard()
lives = Lives()


def shoot_new_beam():
    laser.shoot(position=cannon.position())


# Cannon move
screen.listen()
screen.onkey(cannon.go_left, "Left")
screen.onkey(cannon.go_right, "Right")

screen.onkey(shoot_new_beam, "Up")

# Create alien ships
alien_ships = []


def create_ships():
    for x in range(-240, 250, 45):
        for y in range(0, 170, 40):
            alien = Alien((x, y))
            alien_ships.append(alien)


create_ships()

# Create bunkers
offset = 75
bunker_x_axis = -325
bunker_y_axis = -175
all_bunkers = []
# Creating 4 bunkers:
for b in range(4):
    single_bunker = []
    # Create single bunker from stretched squares:
    for x in range(15):
        for y in range(3):
            bunker = Bunker((bunker_x_axis, bunker_y_axis))
            single_bunker.append(bunker)
            bunker_y_axis += 20
        bunker_y_axis = -175
        bunker_x_axis += 7
    bunker_x_axis += offset
    all_bunkers.append(single_bunker)



round = 0
step = 5
game_is_on = True
while game_is_on:
    screen.update()
    laser.move()
    alien_shot.move()

    # Laser beam collides with alien spaceship
    for s in alien_ships:
        if s.distance(laser) < 18:
            alien_ships.remove(s)
            s.hit()
            laser.reset()
            scoreboard.point()
        elif s.distance(cannon) < 30:
            game_is_on = False
    # Laser beam collides with bunker:
    for bunker in all_bunkers:
        for b in bunker:
            if b.distance(laser) < 5:
                laser.reset()
                b.destroy()
            elif b.distance(alien_shot) < 5: # Alien shot collision with bunker
                alien_shot.reset()
                b.destroy()

    # The alien spaceships move right, left and down:
    round += 1
    if round % 10 == 0:
        step += 1
        if step <= 10:
            for ship in alien_ships:
                ship.move_right()
        elif 10 < step < 20:
            for ship in alien_ships:
                ship.move_left()
        elif step == 20:
            step = 1
            for ship in alien_ships:
                ship.move_down()

    # Alien shoot:
    if round % 100 == 0:
        attacker = random.choice(alien_ships)
        alien_shot.shoot((attacker.xcor(), attacker.ycor()))

    # Cannon gets shot:
    if cannon.distance(alien_shot) < 30:
        alien_shot.reset()
        lives.loose_life()

    if lives.score == 0:
        game_is_on = False

screen.exitonclick()
