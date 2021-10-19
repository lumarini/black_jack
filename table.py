import pygame
import random

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (163, 41, 29)
GREEN = (5, 80, 82)
GREY = (120, 120, 120)
LIGHT_GREY = (200, 200, 200)
DARK_GREY = (80, 80, 80)
YELLOW = (236, 239, 164)

#DISPLAY CONFIGURATION
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("BlackJack")
gameDisplay.fill(GREEN)
clock = pygame.time.Clock()

# FONT
pygame.font.init()
large_font = pygame.font.SysFont("Consolas", 48)
small_font = pygame.font.SysFont("Consolas", 36)
game_font = pygame.font.SysFont("Consolas", 18)

#BACK OF CARD:
backofcard = pygame.image.load("backofcard.png")

#SUITS
icon_diamonds = "♦"
icon_hearts = "♥"
icon_clubs = "♣"
icon_spades = "♠"
# Cards dimensions:
card_width = 80
card_height = 120
# Cards' positions:
dealer_ypos = 80
player_ypos = 320
xpos_2 = [200,320]
xpos_3 = [160,260,360]
xpos_4 = [60, 160,260,360]
xpos_5 = [60,160,260,360,460]


#Add text:
def add_text(x, y, text, font, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    gameDisplay.blit(text_surface, text_rect)

#Shuffled deck for the beginning of the game:
deck = []

def create_deck():
  suits = ["♦","♥","♣","♠"]
  ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
  for rank in ranks:
    for suit in suits:
      try:
        deck.append((rank,suit,int(rank)))
      except ValueError:
        deck.append((rank,suit,10))
      finally:
        random.shuffle(deck)

class Button:
    def __init__(self, x, y, name):
        pygame.draw.rect(gameDisplay, DARK_GREY, [x+5, y+5, 60, 30],0,5)
        pygame.draw.rect(gameDisplay, GREY, [x, y, 60, 30],0,5)
        add_text(x + 30, y + 18, name, game_font, WHITE)

def back_of_card(x,y):
    gameDisplay.blit(backofcard, (x, y))

def get_mouse_position():
    mouse = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    mouse_xpos = mouse[0]
    mouse_ypos = mouse[1]

class Card:
    def __init__(self, cardtuple):
        self.rank = cardtuple[0]
        self.suit = cardtuple[1]
        self.value = cardtuple[2]
        self.text = self.rank + self.suit
        if self.suit == "♣" or self.suit == "♠":
            self.color = BLACK
        else:
            self.color = RED

    def draw_card(self, xpos, ypos):
        pygame.draw.rect(gameDisplay, WHITE, pygame.Rect(xpos, ypos, card_width, card_height),0,8)
        pygame.draw.rect(gameDisplay, self.color, pygame.Rect(xpos + 5, ypos + 5, card_width - 10, card_height - 10), 2, 5)
        add_text(xpos + card_width / 2, ypos + card_height / 2, self.text, small_font, self.color)

def get_first_cards():
    player_card_1 = Card(deck[0])
    player_card_1.draw_card(xpos_2[0], player_ypos)
    player_card_2 = Card(deck[1])
    player_card_2.draw_card(xpos_2[1], player_ypos)
    dealer_card_1 = Card(deck[2])
    dealer_card_1.draw_card(xpos_2[0], dealer_ypos)
    pygame.display.flip()


player_score = 0
dealer_score = 0

def base_text():
    add_text(500, 120, "DEALER", game_font, YELLOW)
    add_text(500, 180, f"{dealer_score}", large_font, YELLOW)
    add_text(500, 340, "PLAYER", game_font, YELLOW)
    add_text(500, 400, f"{player_score}", large_font, YELLOW)

def placeholder():
    for pos in xpos_2:
        back_of_card(pos,dealer_ypos)
        back_of_card(pos,player_ypos)

create_deck()
base_text()
placeholder()
deal_button = Button(100, 240, "Deal")
pygame.display.flip()
# stand_button = Button(200, 240, "Stand")
# hit_button = Button(300, 240, "Hit")
# split_button = Button(400, 240, "Split")

game_over = False
while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                get_first_cards()
                # if event.key == pygame.K_RIGHT:
                #     player_x_change += player_speed
                # if event.key == pygame.K_UP:
                #     if obstacle_speed <= increased_obstacle_speed:
                #         obstacle_speed += 1
                # if event.key == pygame.K_DOWN:
                #     if obstacle_speed >= decreased_obstacle_speed:
                #         obstacle_speed -= 1


pygame.display.update()
clock.tick(60)


pygame.quit()
quit()