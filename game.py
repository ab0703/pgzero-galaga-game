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

#function to draw game state
def draw():
    if lives > 0:
        screen.clear()
        screen.fill('orange')
        ship.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        display_score()
    else:
        game_over_screen()



#function to update game state
def update():
    global score,lives

    #move ship left or right
    if keyboard.left:
        ship.x -= speed
        if ship.x <=0:
            ship.x = 0
    elif keyboard.right:
        ship.x += speed
        if ship.x >= WIDTH:
            ship.x = WIDTH

    #Move bullets
    for bullet in bullets:
        if bullet.y <=0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

    #move the enemies
    for enemy in enemies:
        enemy.y += 5
        if enemy.y >= HEIGHT:
            enemy.x = random.randint(0,WIDTH - 80)
            enemy.y = random.randint(-100,0)
        #check for collision with bullets
        for bullet in bullets:
            if enemy.colliderect(bullet):
                sounds.eep.play()
                score += 100
                bullets.remove(bullet)
                enemies.remove(enemy)
        
        #check for collisions with ship
        if enemy.colliderect(ship):
            lives -=1
            enemies.remove(enemy)
            if lives == 0:
                is_game_over = True
        
    #continously create new enemies
    if len(enemies) < 8:
        enemy = Actor('enemy')
        enemy.x = random.randint(0,WIDTH - 80)
        enemy.y = random.randint(-100,0)
        enemies.append(enemy)

def game_over_screen():
    screen.clear()
    screen.fill('black')
    screen.draw.text('GAME OVER',(CENTER_X - 150, CENTER_Y - 50),fontsize = 60,color = 'blue')


    



















pgzrun.go()

        