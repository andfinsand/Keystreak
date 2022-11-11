import pygame
import keyboard

pygame.init() # will initialize the font module

# WIDTH , HEIGHT = 275 , 120 (this was the original box size before bg)
WIDTH , HEIGHT = 1035 , 689
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
bg_img = pygame.image.load('Images/bg.jpg')
bg_img = pygame.transform.scale(bg_img,(WIDTH, HEIGHT))
pygame.display.set_caption("Keystreak")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
current_streak_font = pygame.font.SysFont("cambria", 30)
previous_streak_font = pygame.font.SysFont("cambria", 20)

# Text for current, last, and highest consecutive key strokes.

def current_streak(streak_value):
    value = current_streak_font.render("Current Streak: " + str(streak_value), True, WHITE)
    WIN.blit(value, [10, 10])

def last_streak(last_streak_value):
    value = previous_streak_font.render("Last Streak: " + str(last_streak_value), True, WHITE)
    WIN.blit(value, [10, 60])

def highest_streak(highest_streak_value):
    value = previous_streak_font.render("Highest Streak: " + str(highest_streak_value), True, WHITE)
    WIN.blit(value, [10, 85])

# Game loop

def main():

    streak_value = 0
    last_streak_value = 0
    highest_streak_value = 0

    run = True
    while run:
        WIN.blit(bg_img,(0,0)) # background image loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Count strokes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if streak_value != 0:
                        last_streak_value = streak_value
                    if streak_value > highest_streak_value:
                        highest_streak_value = streak_value
                    streak_value = 0
                else: # enter all other keys here (letters, numbers, space, enter). Consider one last else statement to continue if any other key.
                    streak_value += 1

        current_streak(streak_value)
        last_streak(last_streak_value)
        highest_streak(highest_streak_value)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

# TO DO:
# Count key strokes for only letters, numbers, return, space and backspace.
# How to make it work while typing in different app.
# Styling - colors, font, background