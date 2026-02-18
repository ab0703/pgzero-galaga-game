import pgzrun
import random


WIDTH =  1200
HEIGHT = 600
CENTER_X = WIDTH//2
CENTER_Y = HEIGHT//2
CENTER = (CENTER_X,CENTER_Y)

TITLE = 'Galaga game'

# game variables
score = 0
lives = 3
is_game_over = False
speed = 5

bullets = []
enemies = []

#create a ship
ship = Actor('spaceship')
ship.pos = (CENTER_X,HEIGHT - 60)

#create the enemies
for i in range(8):
    enemy = Actor('enemy')
    enemy.x = random.randint(0,WIDTH - 80)
    enemy.y = random.randint(-100,0)
    enemies.append(enemy)

#display score
def display_score():
    screen.draw.text(f'Score:{score}',(50,30))
    screen.draw.text(f'lives:{lives}',(50,60))

#create bullets
def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor('bullet')
        bullet.x = ship.x
        bullet.y = ship.y - 50
        bullets.append(bullet)
        