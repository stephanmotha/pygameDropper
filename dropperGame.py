#Charity Choice
#Character collects money and
#decides whether to donate or not
#@date 2017/1/9
import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
VIOLET = (77, 13, 150)
LIGHTBLUE = (153, 217, 234)
GREEN = (0, 255, 0)
GRASS_GREEN = (62, 109, 49)
HILL_GREEN = (31, 99, 52)
SUN = (255, 242, 0)
MOON = (180, 187, 198)
BROWN = (79, 39, 6)
PEACH = (255, 192, 145)
PI = 3.141592653
money_list = []
money_fall_speed = 0.50
ellipse_x = 0
ellipse_y = 0
ellipse_change_x = 1
ellipse_change_y = 0.75
x_coord = 500
y_coord = 600
x_speed = 0
y_speed = 0
score = 0
snow_list = []
for i in range(200):
        x = random.randrange(0, 1000)
        y = random.randrange(0, 750)
        snow_list.append([x, y])
#Classes
class Money:
        pos = [100, 100]
        colour = (0, 255, 0)
        def __init__(self, newColour=GREEN):
                self.colour = newColour
        def draw(self):
                x = self.pos[0]
                y = self.pos[1]
                pygame.draw.rect(screen, self.colour, [x, y, 30, 15])
        def move(self):
                self.pos[1] += random.randint(1,2)
        def checkCollision(self, otherObject, tolerance):
                result = False
                x = self.pos[0]
                y = self.pos[1]
                if (abs(x_coord - x) < tolerance and abs(y_coord - y) < tolerance):
                        result = True
                return result
        
class Person:
        pos = [500, 600]
        colour = (0, 0, 255)
        def _init_(self, newColour=BLUE):
                self.colour = newColour
        def draw(self):
                pygame.draw.ellipse(screen, PEACH, [x_coord, y_coord, 20, 20], 0)
                pygame.draw.rect(screen, self.colour, [x_coord, y_coord+20, 20, 40])
                pygame.draw.rect(screen, BLACK, [x_coord, y_coord+60, 8, 35])
                pygame.draw.rect(screen, BLACK, [x_coord+12, y_coord+60, 8, 35])
                pygame.draw.rect(screen, BLUE, [x_coord-5, y_coord+20, 5, 30])
                pygame.draw.rect(screen, BLUE, [x_coord+20, y_coord+20, 5, 30])
                
pygame.init()
 
# Setting the width and height of the screen [width, height]
size = (1000, 750)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Charity Choice")
 
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
moneyList = [Money()]
for i in range(50):
        money = Money()
        money.pos = [random.randrange(50, 950), random.randrange(-750, 0)]
        moneyList.append(money)
George = Person()
# -------- Main Program Loop -----------
while not done:
        # --- Main event loop
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN:
                        # Figure out if it was an arrow key. If so
                        # adjust speed.
                        if event.key == pygame.K_LEFT:
                                x_speed = -3
                        elif event.key == pygame.K_RIGHT:
                                x_speed = 3
                        elif event.key == pygame.K_UP:
                                y_speed = -3
                        elif event.key == pygame.K_DOWN:
                                y_speed = 3
        
        # User let up on a key
                elif event.type == pygame.KEYUP:
                        # If it is an arrow key, reset vector back to zero
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                x_speed = 0
                        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                y_speed = 0
        if x_coord < 0:
                if event.key == pygame.K_LEFT:
                        x_speed = 0
        elif x_coord > 1000:
                if event.key == pygame.K_RIGHT:
                        x_speed = 0
        if y_coord < 550:
                if event.key == pygame.K_UP:
                        y_speed = 0
        elif y_coord > 700:
                if event.key == pygame.K_DOWN:
                        y_speed = 0
        # Move the object according to the speed vector.
        x_coord += x_speed
        y_coord += y_speed
        for money in moneyList:
                money.move()
        if money.pos[1] > 750:
                money.pos[1] = random.randrange(-750,0)
        for money in moneyList:
                if money.checkCollision(George, 20) == True:
                        moneyList.remove(money)
                        score = score + 1
        
                screen.fill(LIGHTBLUE)
                pygame.mouse.set_visible(False)
#Drawing Code

#Snowflakes
        for i in range(len(snow_list)):
        # Draw the snow flake
                pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        # Move the snow flake down one pixel
                snow_list[i][1] += 1
        # If the snow flake has moved off the bottom of the screen
                if snow_list[i][1] > 750:
                # Reset it just above the top
                        y = random.randrange(-50, -10)
                        snow_list[i][1] = y
                # Give it a new x position
                        x = random.randrange(20, 980)
                        snow_list[i][0] = x
#Hills
        x_offset = 0
        y_offset = 0
        while x_offset < 300:
                pygame.draw.ellipse(screen, HILL_GREEN, [x_offset-50, y_offset+400, 400, 300])
                x_offset = x_offset + 200
                y_offset = y_offset + 75
#Sun
        pygame.draw.ellipse(screen, SUN, [ellipse_x,ellipse_y,100,100])
        ellipse_x += ellipse_change_x
        ellipse_y += ellipse_change_y
        if ellipse_x > 1000 or ellipse_x < -50:
                ellipse_x = -35
                ellipse_y = -35
                if SUN == (255, 242, 0):
                        SUN = (180, 187, 198)
                        LIGHTBLUE = (5, 31, 73)
                elif SUN == (180, 187, 198):
                        SUN = (255, 242, 0)
                        LIGHTBLUE = (153, 217, 234)
#Grass
        pygame.draw.rect(screen, GRASS_GREEN, [0, 600, 1000, 150])
#Snow
        pygame.draw.rect(screen, WHITE, [0, 575, 1000, 25])
#Tree
        pygame.draw.ellipse(screen, HILL_GREEN, [750, 200, 175, 175])
        pygame.draw.rect(screen, BROWN, [825, 370, 25, 205])
#Clouds
        x_offset = 0
        while x_offset < 500:
                pygame.draw.ellipse(screen, WHITE, [100+x_offset,25,100,75])
                pygame.draw.ellipse(screen, WHITE, [125+x_offset,50,100,75])
                pygame.draw.ellipse(screen, WHITE, [145+x_offset,20,100,75])
                x_offset = x_offset + 200
#Snowman
        pygame.draw.ellipse(screen, WHITE, [700,500,100,100])
        pygame.draw.ellipse(screen, WHITE, [712,450,75,75])
        pygame.draw.ellipse(screen, WHITE, [724,412,50,50])
        x_offset = 0
        while x_offset < 40:
                pygame.draw.ellipse(screen, BLACK, [737+x_offset,425,5,5])
                x_offset = x_offset+20
                pygame.draw.arc(screen, BLACK,  [737,425,25,25],  PI, 3*PI/2, 2)
                pygame.draw.arc(screen, BLACK,  [737,425,25,25],  3*PI/2, 2*PI, 2)
                y_offset = 0
        while y_offset < 60:
                pygame.draw.ellipse(screen, BLACK, [747,467+y_offset,5,5])
                y_offset = y_offset + 20
                pygame.draw.line(screen, BLACK, [715,412], [780,412], 10)
                pygame.draw.rect(screen, BLACK, [730,350,35,63])
                pygame.draw.polygon(screen, ORANGE, [[750,430], [725,435], [750,440]])
        for money in moneyList:
                money.draw()

        if moneyList == []:
                done = True
        George.draw()

#Game Title
        font = pygame.font.SysFont('Calibri', 35, True, False)
        text = font.render("Charity Choice Game", True, VIOLET)
        screen.blit(text, [25, 300])
# --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

# --- Limit to 60 frames per second
        clock.tick(60)

# Close the window and quit.
pygame.quit()
print("Your score is " + str(score))
print("Congratulations, you won!")


