import pygame

BGCOLOR = "#01937C"
WHITE = "#F9F9F9"
BLACK = "#343A40"
RED = "#F55C47"

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Black Jack")
gameDisplay.fill(BGCOLOR)
clock = pygame.time.Clock()

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

            print(event)

    pygame.display.update()
    clock.tick(60)     # number of FPS


# def start_game():
#     pass

# card_back = PhotoImage(file='backcard.png')
# card_front = PhotoImage(file='frontcard.png')
#
# canvas.create_image(200, 100, image=card_front)
# canvas.pack()


# start_game_button = Button(text="Start Game", highlightthickness=0)
# start_game_button.grid(column=1, row=1,columnspan=2)



pygame.quit()
quit()