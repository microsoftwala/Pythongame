import time
import pygame
import random

pygame.init()


# Create the screen
screen = pygame.display.set_mode((900, 620))

# Title and Icon
pygame.display.set_caption("Stone Paper Scissors")
icon = pygame.image.load("paper.png")
pygame.display.set_icon(icon)

# Load background image
background = pygame.image.load("table.png")
background = pygame.transform.scale(background, (850, 510))

# player
playerImg = pygame.image.load("hand1.png")
playerImg1 = pygame.image.load("hand2.png")
playerImg2 = pygame.image.load("hand3.png")
# Image will came from left
playerImg = pygame.transform.rotate(playerImg, 270)
playerImg1 = pygame.transform.rotate(playerImg1, 270)
playerImg2 = pygame.transform.rotate(playerImg2, 270)
# Image will came from right
playerImg3 = pygame.transform.rotate(playerImg, 180)
playerImg4 = pygame.transform.rotate(playerImg1, 180)
playerImg5 = pygame.transform.rotate(playerImg2, 180)
# Image will came from top
playerImg6 = pygame.transform.rotate(playerImg, -90)
playerImg7 = pygame.transform.rotate(playerImg1, -90)
playerImg8 = pygame.transform.rotate(playerImg2, -90)
# Image will came diagonal left
playerImg9 = pygame.transform.rotate(playerImg, 45)
playerImg10 = pygame.transform.rotate(playerImg1, 45)
playerImg11 = pygame.transform.rotate(playerImg2, 45)
# Image will came diagonal right
playerImg12 = pygame.transform.rotate(playerImg, 135)
playerImg13 = pygame.transform.rotate(playerImg1, 135)
playerImg14 = pygame.transform.rotate(playerImg2, 135)
# Image will came from down
playerImg15 = pygame.transform.rotate(playerImg, 90)
playerImg15 = pygame.transform.rotate(playerImg1, 90)
playerImg17 = pygame.transform.rotate(playerImg2, 90)

# Two player
# Left paper
posX = 50
posY = 200  # not changed

# Left scissor
posX1 = 50
posY1 = 200  # not changed

# Left stone
posX2 = 50
posY2 = 200  # not changed

# right paper
posX3 = 750
posY3 = 200  # not changed

# right scissor
posX4 = 750
posY4 = 200  # not changed

# right stone
posX5 = 750
posY5 = 200  # not changed


# Three Player
# top paper
pos3X = 350  # not changed
pos3Y = 0

# top scissor
pos3X1 = 350  # not changed
pos3Y1 = 0

# top stone
pos3X2 = 350  # not changed
pos3Y2 = 0

# left paper
pos3X3 = 50
pos3Y3 = 400

# left scissor
pos3X4 = 50
pos3Y4 = 400

# left stone
pos3X5 = 50
pos3Y5 = 400

# right paper
pos3X6 = 650
pos3Y6 = 400

# right scissor
pos3X7 = 650
pos3Y7 = 400

# right stone
pos3X8 = 650
pos3Y8 = 400


# Four player
# Left paper
pos4X = 50
pos4Y = 200  # not changed

# Left scissor
pos4X1 = 50
pos4Y1 = 200  # not changed

# Left stone
pos4X2 = 50
pos4Y2 = 200  # not changed

# right paper
pos4X3 = 750
pos4Y3 = 200  # not changed

# right scissor
pos4X4 = 750
pos4Y4 = 200  # not changed

# right stone
pos4X5 = 750
pos4Y5 = 200   # not changed

# top paper
pos4X6 = 350  # not changed
pos4Y6 = 0

# top scissor
pos4X7 = 350    # not changed
pos4Y7 = 0

# top stone
pos4X8 = 350  # not changed
pos4Y8 = 0

# down paper
pos4X9 = 350  # not changed
pos4Y9 = 500

# down scissor
pos4X10 = 350  # not changed
pos4Y10 = 500

# down stone
pos4X11 = 350  # not changed
pos4Y11 = 500


start = 0  # when two player
start1 = 0  # when three player
start2 = 0  # when four player

hand_type = 0


def player(playerImg, posX, posY):
    screen.blit(playerImg, (posX, posY))


# It is among four player decider
def decider4(user_choice, player2_choice, player3_choice, player4_choice):
    choices = [user_choice, player2_choice, player3_choice, player4_choice]
    if choices.count(user_choice) == 4:
        return "It's a tie among all players!"
    elif choices.count(user_choice) == 1:
        return "You win!"  # User wins against all other players
    else:
        return "It's a tie among some players."


# It is among three player decider
def decider3(user_choice, player2_choice, player3_choice):
    if user_choice == player2_choice == player3_choice:
        return "It's a tie among all players!"
    elif user_choice == player2_choice or user_choice == player3_choice:
        return "You win!"  # User wins against at least one other player
    elif player2_choice == player3_choice:
        return "Player 2 and Player 3 tie!"
    else:
        return "It's a tie among all players!"


# It is among two player decider
def decider(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissor" else "Computer wins!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    elif user_choice == "scissor":
        return "You win!" if computer_choice == "paper" else "Computer wins!"


fonts = pygame.font.SysFont('Georgia', 40, bold=True)
fonts1 = pygame.font.SysFont('Georgia', 40, bold=True)
fonts2 = pygame.font.SysFont('Georgia', 20)

message = fonts2.render("Enter the number of player: ", True, 'white')
surf = fonts.render('Quit', True, 'white')
surf1 = fonts1.render('Start', True, 'white')
Paper_B = fonts2.render('Paper', True, 'white')
Scissor_B = fonts2.render('Scissor', True, 'white')
Rock_B = fonts2.render('Rock', True, 'white')
back = fonts2.render("Back", True, 'white')

button = pygame.Rect(600, 550, 105, 60)
Start_button = pygame.Rect(200, 550, 115, 60)
Paper_button = pygame.Rect(200, 500, 62, 35)
Scissor_button = pygame.Rect(400, 500, 77, 35)
Rock_button = pygame.Rect(600, 500, 62, 35)
button5 = pygame.Rect(350, 100, 150, 40)
back_button = pygame.Rect(820, 5, 60, 25)


animation_speed = 0.3
animation_speed1 = 0.3
animation_speed2 = 0.3
animation_speed3 = -0.3
animation_speed4 = -0.3
animation_speed5 = -0.3


player1_choice_selected = False
player2_choice_selected = False

count_player = pygame.font.SysFont('Georgia', 20, bold=True)
player_count = ''
on = 0
option = 1


# Result show after match
def Show_result(Ans, pos3Y):
    surf5 = fonts2.render(Ans, True, 'white')
    button5 = pygame.Rect(350, 100, 150, 40)
    if pos3Y >= 110:
        screen.blit(surf5, (button5.x + 5, button5.y - 20))


# Rock paper scissor button
def buttonlaga(a, b):
    if Paper_button.x <= a <= Paper_button.x + 110 and Paper_button.y <= b <= Paper_button.y + 60:
        pygame.draw.rect(screen, (0, 0, 100),
                         Paper_button, border_radius=3)
        screen.blit(Paper_B, (Paper_button.x + 6.5, Paper_button.y + 6.5))
    else:
        pygame.draw.rect(screen, (10, 10, 10),
                         Paper_button, border_radius=3)
        screen.blit(Paper_B, (Paper_button.x + 5, Paper_button.y + 5))

    if Scissor_button.x <= a <= Scissor_button.x + 110 and Scissor_button.y <= b <= Scissor_button.y + 60:
        pygame.draw.rect(screen, (0, 0, 100),
                         Scissor_button, border_radius=3)
        screen.blit(Scissor_B, (Scissor_button.x +
                    6.5, Scissor_button.y + 6.5))
    else:
        pygame.draw.rect(screen, (10, 10, 10),
                         Scissor_button, border_radius=3)
        screen.blit(Scissor_B, (Scissor_button.x + 5, Scissor_button.y + 5))

    if Rock_button.x <= a <= Rock_button.x + 110 and Rock_button.y <= b <= Rock_button.y + 60:
        pygame.draw.rect(screen, (0, 0, 100), Rock_button, border_radius=3)
        screen.blit(Rock_B, (Rock_button.x + 6.5, Rock_button.y + 6.5))
    else:
        pygame.draw.rect(screen, (10, 10, 10), Rock_button, border_radius=3)
        screen.blit(Rock_B, (Rock_button.x + 5, Rock_button.y + 5))


# gradient backgrounds
def gradientRect(screen, left_colour, right_colour, target_rect):
    # Create a gradient surface with the same dimensions as the target_rect
    gradient_surface = pygame.Surface((target_rect.width, target_rect.height))
    # Define the left and right color stops
    left_color_stop = left_colour
    right_color_stop = right_colour
    # Fill the gradient surface with a horizontal gradient
    for x in range(target_rect.width):
        # Calculate the interpolation factor
        factor = x / (target_rect.width - 1)
        # Interpolate between left and right colors
        r = int(left_color_stop[0] + factor *
                (right_color_stop[0] - left_color_stop[0]))
        g = int(left_color_stop[1] + factor *
                (right_color_stop[1] - left_color_stop[1]))
        b = int(left_color_stop[2] + factor *
                (right_color_stop[2] - left_color_stop[2]))

        # Draw a vertical line of the gradient color
        pygame.draw.line(gradient_surface, (r, g, b),
                         (x, 0), (x, target_rect.height))

    # Blit the gradient surface onto the screen at the target_rect position
    screen.blit(gradient_surface, target_rect)


target_rect = pygame.Rect(0, 0, 900, 620)

# Game Loop
running = True

while running:
    # Set the background
    gradientRect(screen, (150, 100, 40), (0, 150, 200), target_rect)

    # set background picture
    screen.blit(background, (25, 35))

    if option == 1:
        screen.blit(message, (0, 0))
    if option == 0:
        if back_button.x <= a <= back_button.x + 110 and back_button.y <= b <= back_button.y + 60:
            pygame.draw.rect(screen, (200, 100, 0),
                             back_button, border_radius=3)
            screen.blit(back, (back_button.x+8, back_button.y+1))
        else:
            pygame.draw.rect(screen, (0, 0, 0),
                             back_button, border_radius=3)
            screen.blit(back, (back_button.x+7, back_button.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            player_count = 0
            player_count = event.unicode
            on = 1

        if event.type == pygame.MOUSEBUTTONUP:
            if back_button.collidepoint(event.pos):
                option = 1  # showing option How many player will play
                on = 0  # off

        if player_count == '2' and event.type == pygame.MOUSEBUTTONUP:
            if button.collidepoint(event.pos):
                pygame.quit()
            if Start_button.collidepoint(event.pos):
                start = 1
                start1 = 0
                start2 = 0
                hand_type = 0
                animation_speed = 0.3
                animation_speed1 = 0.3
                animation_speed2 = 0.3
                animation_speed3 = -0.3
                animation_speed4 = -0.3
                animation_speed5 = -0.3
                posX = 50
                posX1 = 50
                posX2 = 50
                posX3 = 750
                posX4 = 750
                posX5 = 750
                Paper_button.topleft = (200, 500)
                Scissor_button.topleft = (420, 500)
                Rock_button.topleft = (650, 500)
            if start:  # Check if the "Start" button is clicked
                # if not player1_choice_selected:
                if Paper_button.collidepoint(event.pos):
                    hand_type = 1
                    computer_turn = random.randint(0, 2)
                    Paper_button.topleft = (-100, -100)  # disappear button
                    Scissor_button.topleft = (-100, -100)  # disappear button
                    Rock_button.topleft = (-100, -100)  # disappear button
                if Scissor_button.collidepoint(event.pos):
                    hand_type = 2
                    computer_turn = random.randint(0, 2)
                    Paper_button.topleft = (-100, -100)  # disappear button
                    Scissor_button.topleft = (-100, -100)  # disappear button
                    Rock_button.topleft = (-100, -100)  # disappear button
                if Rock_button.collidepoint(event.pos):
                    hand_type = 3
                    computer_turn = random.randint(0, 2)
                    Paper_button.topleft = (-100, -100)  # disappear button
                    Scissor_button.topleft = (-100, -100)  # disappear button
                    Rock_button.topleft = (-100, -100)  # disappear button

        if player_count == '3' and event.type == pygame.MOUSEBUTTONUP:
            if button.collidepoint(event.pos):
                pygame.quit()
            if Start_button.collidepoint(event.pos):
                start1 = 1
                start = 0
                start2 = 0
                hand_type = 0
                animation_speed = 0.3
                animation_speed1 = 0.3
                animation_speed2 = 0.3
                animation_speed3 = -0.3
                animation_speed4 = -0.3
                animation_speed5 = -0.3
                pos3Y = 0
                pos3Y1 = 0
                pos3Y2 = 0
                pos3X3 = 50
                pos3Y3 = 400
                pos3X4 = 50
                pos3Y4 = 400
                pos3X5 = 50
                pos3Y5 = 410
                pos3X6 = 630
                pos3Y6 = 410
                pos3X7 = 630
                pos3Y7 = 410
                pos3X8 = 630
                pos3Y8 = 410
                Paper_button.topleft = (200, 500)
                Scissor_button.topleft = (420, 500)
                Rock_button.topleft = (650, 500)
            if start1:
                if Paper_button.collidepoint(event.pos):
                    hand_type = 1
                    computer_turn = random.randint(0, 2)
                    computer_turn1 = random.randint(0, 2)
                    Paper_button.topleft = (-100, -100)  # disappear button
                    Scissor_button.topleft = (-100, -100)  # disappear button
                    Rock_button.topleft = (-100, -100)  # disappear button
                if Scissor_button.collidepoint(event.pos):
                    hand_type = 2
                    computer_turn = random.randint(0, 2)
                    computer_turn1 = random.randint(0, 2)
                    Paper_button.topleft = (-100, -100)  # disappear button
                    Scissor_button.topleft = (-100, -100)  # disappear button
                    Rock_button.topleft = (-100, -100)  # disappear button
                if Rock_button.collidepoint(event.pos):
                    hand_type = 3
                    computer_turn = random.randint(0, 2)
                    computer_turn1 = random.randint(0, 2)
                    Paper_button.topleft = (-100, -100)  # disappear button
                    Scissor_button.topleft = (-100, -100)  # disappear button
                    Rock_button.topleft = (-100, -100)  # disappear button

        if player_count == '4' and event.type == pygame.MOUSEBUTTONUP:
            if button.collidepoint(event.pos):
                pygame.quit()
            if Start_button.collidepoint(event.pos):
                start2 = 1
                start1 = 0
                start = 0
                hand_type = 0
                animation_speed = 0.3
                animation_speed1 = 0.3
                animation_speed2 = 0.3
                animation_speed3 = -0.3
                animation_speed4 = -0.3
                animation_speed5 = -0.3
                pos4Y8 = 0
                pos4Y7 = 0
                pos4Y6 = 0
                pos4Y9 = 500
                pos4Y10 = 500
                pos4Y11 = 500
                pos4X5 = 750
                pos4X4 = 750
                pos4X3 = 750
                pos4X2 = 50
                pos4X1 = 50
                pos4X = 50
                Paper_button.topleft = (200, 500)
                Scissor_button.topleft = (430, 500)
                Rock_button.topleft = (650, 500)
            if start2:
                if Paper_button.collidepoint(event.pos):
                    hand_type = 1
                    computer_turn = random.randint(0, 2)
                    computer_turn1 = random.randint(0, 2)
                    computer_turn2 = random.randint(0, 2)
                    Paper_button.topleft = (-100, -100)  # disappear button
                    Scissor_button.topleft = (-100, -100)  # disappear button
                    Rock_button.topleft = (-100, -100)  # disappear button
                if Scissor_button.collidepoint(event.pos):
                    hand_type = 2
                    computer_turn = random.randint(0, 2)
                    computer_turn1 = random.randint(0, 2)
                    computer_turn2 = random.randint(0, 2)
                    Paper_button.topleft = (-100, -100)  # disappear button
                    Scissor_button.topleft = (-100, -100)  # disappear button
                    Rock_button.topleft = (-100, -100)  # disappear button
                if Rock_button.collidepoint(event.pos):
                    hand_type = 3
                    computer_turn = random.randint(0, 2)
                    computer_turn1 = random.randint(0, 2)
                    computer_turn2 = random.randint(0, 2)
                    Paper_button.topleft = (-100, -100)  # disappear button
                    Scissor_button.topleft = (-100, -100)  # disappear button
                    Rock_button.topleft = (-100, -100)  # disappear button

    if on == 1:

        a, b = pygame.mouse.get_pos()
        option = 0
        text_surface = count_player.render(player_count, True, (0, 0, 0))
        screen.blit(text_surface, (0, 0))

        if button.x <= a <= button.x + 110 and button.y <= b <= button.y + 60:
            pygame.draw.rect(screen, (200, 50, 0), button, border_radius=3)
            screen.blit(surf, (button.x + 7.5, button.y + 7.5))
        else:
            pygame.draw.rect(screen, (0, 0, 0), button, border_radius=3)
            screen.blit(surf, (button.x + 5, button.y + 5))

        if Start_button.x <= a <= Start_button.x + 110 and Start_button.y <= b <= Start_button.y + 60:
            pygame.draw.rect(screen, (100, 200, 50),
                             Start_button, border_radius=3)
            screen.blit(surf1, (Start_button.x + 7.5, Start_button.y + 7.5))
        else:
            pygame.draw.rect(screen, (0, 0, 0), Start_button, border_radius=3)
            screen.blit(surf1, (Start_button.x + 5, Start_button.y + 5))

        if start and player_count == '2':
            buttonlaga(a, b)
            users = ""
            computer = ""

            if hand_type == 1:
                posX += animation_speed
                user = "paper"
                if posX >= 200:
                    animation_speed = 0
                player(playerImg, posX, posY)
                if computer_turn == 0:
                    computer = "paper"
                    posX3 += animation_speed3
                    if posX3 <= 550:
                        animation_speed3 = 0
                    player(playerImg3, posX3, 200)
                elif computer_turn == 1:
                    computer = "scissor"
                    posX3 += animation_speed3
                    if posX3 <= 550:
                        animation_speed3 = 0
                    player(playerImg4, posX3, 200)
                elif computer_turn == 2:
                    computer = "rock"
                    posX3 += animation_speed3
                    if posX3 <= 550:
                        animation_speed3 = 0
                    player(playerImg5, posX3, 200)
                Ans = decider(user, computer)
                surf5 = fonts2.render(Ans, True, 'white')
                button5 = pygame.Rect(350, 100, 150, 40)
                if posX3 <= 550:
                    screen.blit(surf5, (button5.x + 5, button5.y + 5))

            if hand_type == 2:
                user = "scissor"
                posX1 += animation_speed1
                if posX1 >= 200:
                    animation_speed1 = 0
                player(playerImg1, posX1, posY1)
                if computer_turn == 0:
                    computer = "paper"
                    posX4 += animation_speed4
                    if posX4 <= 550:
                        animation_speed4 = 0
                    player(playerImg3, posX4, 200)
                elif computer_turn == 1:
                    computer = "scissor"
                    posX4 += animation_speed4
                    if posX4 <= 550:
                        animation_speed4 = 0
                    player(playerImg4, posX4, 200)
                elif computer_turn == 2:
                    computer = "rock"
                    posX4 += animation_speed4
                    if posX4 <= 550:
                        animation_speed4 = 0
                    player(playerImg5, posX4, 200)
                Ans = decider(user, computer)
                surf5 = fonts2.render(Ans, True, 'white')
                button5 = pygame.Rect(350, 100, 150, 40)
                if posX4 <= 550:
                    screen.blit(surf5, (button5.x + 5, button5.y + 5))

            if hand_type == 3:
                posX2 += animation_speed2
                user = "rock"
                if posX2 >= 200:
                    animation_speed2 = 0
                player(playerImg2, posX2, posY2)
                if computer_turn == 0:
                    computer = "paper"
                    posX5 += animation_speed5
                    if posX5 <= 550:
                        animation_speed5 = 0
                    player(playerImg3, posX5, 200)
                elif computer_turn == 1:
                    computer = "scissor"
                    posX5 += animation_speed5
                    if posX5 <= 550:
                        animation_speed5 = 0
                    player(playerImg4, posX5, 200)
                elif computer_turn == 2:
                    computer = "rock"
                    posX5 += animation_speed5
                    if posX5 <= 550:
                        animation_speed5 = 0
                    player(playerImg5, posX5, 200)
                Ans = decider(user, computer)
                surf5 = fonts2.render(Ans, True, 'white')
                button5 = pygame.Rect(350, 100, 150, 40)
                if posX5 <= 550:
                    screen.blit(surf5, (button5.x + 5, button5.y + 5))

        if start1 and player_count == '3':
            buttonlaga(a, b)
            if hand_type == 1:
                pos3X3 += animation_speed
                pos3Y3 -= animation_speed
                user = "paper"
                if pos3X3 >= 220:
                    animation_speed = 0
                player(playerImg9, pos3X3, pos3Y3)
                if computer_turn == 0:
                    computer = "paper"
                    # second computer
                    if computer_turn1 == 0:
                        computer1 = "paper"
                        pos3X6 -= animation_speed2
                        pos3Y6 -= animation_speed2
                        if pos3X6 <= 450:
                            animation_speed2 = 0
                        player(playerImg12, pos3X6, pos3Y6)
                    elif computer_turn1 == 1:
                        computer1 = "scissor"
                        pos3X7 -= animation_speed2
                        pos3Y7 -= animation_speed2
                        if pos3X7 <= 450:
                            animation_speed2 = 0
                        player(playerImg13, pos3X7, pos3Y7)
                    else:
                        computer1 = "rock"
                        pos3X8 -= animation_speed2
                        pos3Y8 -= animation_speed2
                        if pos3X8 <= 450:
                            animation_speed2 = 0
                        player(playerImg14, pos3X8, pos3Y8)
                    pos3Y += animation_speed1
                    if pos3Y >= 110:
                        animation_speed1 = 0
                    player(playerImg6, 350, pos3Y)
                    Ans = decider3(user, computer, computer1)
                    Show_result(Ans, pos3Y2)

                elif computer_turn == 1:
                    computer = "scissor"
                    if computer_turn1 == 0:
                        computer1 = "paper"
                        pos3X6 -= animation_speed2
                        pos3Y6 -= animation_speed2
                        if pos3X6 <= 450:
                            animation_speed2 = 0
                        player(playerImg12, pos3X6, pos3Y6)
                    elif computer_turn1 == 1:
                        computer1 = "scissor"
                        pos3X7 -= animation_speed2
                        pos3Y7 -= animation_speed2
                        if pos3X7 <= 450:
                            animation_speed2 = 0
                        player(playerImg13, pos3X7, pos3Y7)
                    else:
                        computer1 = "rock"
                        pos3X8 -= animation_speed2
                        pos3Y8 -= animation_speed2
                        if pos3X8 <= 450:
                            animation_speed2 = 0
                        player(playerImg14, pos3X8, pos3Y8)
                    pos3Y1 += animation_speed1
                    if pos3Y1 >= 110:
                        animation_speed1 = 0
                    player(playerImg7, 350, pos3Y1)
                    Ans = decider3(user, computer, computer1)
                    Show_result(Ans, pos3Y2)

                elif computer_turn == 2:
                    computer = "rock"
                    if computer_turn1 == 0:
                        computer1 = "paper"
                        pos3X6 -= animation_speed2
                        pos3Y6 -= animation_speed2
                        if pos3X6 <= 450:
                            animation_speed2 = 0
                        player(playerImg12, pos3X6, pos3Y6)
                    elif computer_turn1 == 1:
                        computer1 = "scissor"
                        pos3X7 -= animation_speed2
                        pos3Y7 -= animation_speed2
                        if pos3X7 <= 450:
                            animation_speed2 = 0
                        player(playerImg13, pos3X7, pos3Y7)
                    else:
                        computer1 = "rock"
                        pos3X8 -= animation_speed2
                        pos3Y8 -= animation_speed2
                        if pos3X8 <= 450:
                            animation_speed2 = 0
                        player(playerImg14, pos3X8, pos3Y8)
                    pos3Y2 += animation_speed1
                    if pos3Y2 >= 110:
                        animation_speed1 = 0
                    player(playerImg8, 350, pos3Y2)
                    Ans = decider3(user, computer, computer1)
                    Show_result(Ans, pos3Y2)

            if hand_type == 2:
                user = "scissor"
                pos3X4 += animation_speed
                pos3Y4 -= animation_speed
                if pos3X4 >= 220:
                    animation_speed = 0
                player(playerImg10, pos3X4, pos3Y4)
                if computer_turn == 0:
                    computer = "paper"
                    if computer_turn1 == 0:
                        computer1 = "paper"
                        pos3X6 -= animation_speed2
                        pos3Y6 -= animation_speed2
                        if pos3X6 <= 450:
                            animation_speed2 = 0
                        player(playerImg12, pos3X6, pos3Y6)
                    elif computer_turn1 == 1:
                        computer1 = "scissor"
                        pos3X7 -= animation_speed2
                        pos3Y7 -= animation_speed2
                        if pos3X7 <= 450:
                            animation_speed2 = 0
                        player(playerImg13, pos3X7, pos3Y7)
                    else:
                        computer1 = "rock"
                        pos3X8 -= animation_speed2
                        pos3Y8 -= animation_speed2
                        if pos3X8 <= 450:
                            animation_speed2 = 0
                        player(playerImg14, pos3X8, pos3Y8)
                    pos3Y += animation_speed1
                    if pos3Y >= 110:
                        animation_speed1 = 0
                    player(playerImg6, 350, pos3Y)
                    Ans = decider3(user, computer, computer1)
                    Show_result(Ans, pos3Y)

                elif computer_turn == 1:
                    computer = "scissor"
                    if computer_turn1 == 0:
                        computer1 = "paper"
                        pos3X6 -= animation_speed2
                        pos3Y6 -= animation_speed2
                        if pos3X6 <= 450:
                            animation_speed2 = 0
                        player(playerImg12, pos3X6, pos3Y6)
                    elif computer_turn1 == 1:
                        computer1 = "scissor"
                        pos3X7 -= animation_speed2
                        pos3Y7 -= animation_speed2
                        if pos3X7 <= 450:
                            animation_speed2 = 0
                        player(playerImg13, pos3X7, pos3Y7)
                    else:
                        computer1 = "rock"
                        pos3X8 -= animation_speed2
                        pos3Y8 -= animation_speed2
                        if pos3X8 <= 450:
                            animation_speed2 = 0
                        player(playerImg14, pos3X8, pos3Y8)
                    pos3Y1 += animation_speed1
                    if pos3Y1 >= 110:
                        animation_speed1 = 0
                    player(playerImg7, 350, pos3Y1)
                    Ans = decider3(user, computer, computer1)
                    Show_result(Ans, pos3Y1)

                elif computer_turn == 2:
                    computer = "rock"
                    if computer_turn1 == 0:
                        computer1 = "paper"
                        pos3X6 -= animation_speed2
                        pos3Y6 -= animation_speed2
                        if pos3X6 <= 450:
                            animation_speed2 = 0
                        player(playerImg12, pos3X6, pos3Y6)
                    elif computer_turn1 == 1:
                        computer1 = "scissor"
                        pos3X7 -= animation_speed2
                        pos3Y7 -= animation_speed2
                        if pos3X7 <= 450:
                            animation_speed2 = 0
                        player(playerImg13, pos3X7, pos3Y7)
                    else:
                        computer1 = "rock"
                        pos3X8 -= animation_speed2
                        pos3Y8 -= animation_speed2
                        if pos3X8 <= 450:
                            animation_speed2 = 0
                        player(playerImg14, pos3X8, pos3Y8)
                    pos3Y2 += animation_speed1
                    if pos3Y2 >= 110:
                        animation_speed1 = 0
                    player(playerImg8, 350, pos3Y2)
                    Ans = decider3(user, computer, computer1)
                    Show_result(Ans, pos3Y2)
            if hand_type == 3:
                user = "rock"
                pos3X5 += animation_speed
                pos3Y5 -= animation_speed
                if pos3X5 >= 220:
                    animation_speed = 0
                player(playerImg11, pos3X5, pos3Y5)
                if computer_turn == 0:
                    computer = "paper"
                    if computer_turn1 == 0:
                        computer1 = "paper"
                        pos3X6 -= animation_speed2
                        pos3Y6 -= animation_speed2
                        if pos3X6 <= 450:
                            animation_speed2 = 0
                        player(playerImg12, pos3X6, pos3Y6)
                    elif computer_turn1 == 1:
                        computer1 = "scissor"
                        pos3X7 -= animation_speed2
                        pos3Y7 -= animation_speed2
                        if pos3X7 <= 450:
                            animation_speed2 = 0
                        player(playerImg13, pos3X7, pos3Y7)
                    else:
                        computer1 = "rock"
                        pos3X8 -= animation_speed2
                        pos3Y8 -= animation_speed2
                        if pos3X8 <= 450:
                            animation_speed2 = 0
                        player(playerImg14, pos3X8, pos3Y8)
                    pos3Y += animation_speed1
                    if pos3Y >= 110:
                        animation_speed1 = 0
                    player(playerImg6, 350, pos3Y)
                    Ans = decider3(user, computer, computer1)
                    Show_result(Ans, pos3Y)

                elif computer_turn == 1:
                    computer = "scissor"
                    if computer_turn1 == 0:
                        computer1 = "paper"
                        pos3X6 -= animation_speed2
                        pos3Y6 -= animation_speed2
                        if pos3X6 <= 450:
                            animation_speed2 = 0
                        player(playerImg12, pos3X6, pos3Y6)
                    elif computer_turn1 == 1:
                        computer1 = "scissor"
                        pos3X7 -= animation_speed2
                        pos3Y7 -= animation_speed2
                        if pos3X7 <= 450:
                            animation_speed2 = 0
                        player(playerImg13, pos3X7, pos3Y7)
                    else:
                        computer1 = "rock"
                        pos3X8 -= animation_speed2
                        pos3Y8 -= animation_speed2
                        if pos3X8 <= 450:
                            animation_speed2 = 0
                        player(playerImg14, pos3X8, pos3Y8)
                    pos3Y1 += animation_speed1
                    if pos3Y1 >= 110:
                        animation_speed1 = 0
                    player(playerImg7, 350, pos3Y1)
                    Ans = decider3(user, computer, computer1)
                    Show_result(Ans, pos3Y1)

                elif computer_turn == 2:
                    computer = "rock"
                    if computer_turn1 == 0:
                        computer1 = "paper"
                        pos3X6 -= animation_speed2
                        pos3Y6 -= animation_speed2
                        if pos3X6 <= 450:
                            animation_speed2 = 0
                        player(playerImg12, pos3X6, pos3Y6)
                    elif computer_turn1 == 1:
                        computer1 = "scissor"
                        pos3X7 -= animation_speed2
                        pos3Y7 -= animation_speed2
                        if pos3X7 <= 450:
                            animation_speed2 = 0
                        player(playerImg13, pos3X7, pos3Y7)
                    else:
                        computer1 = "rock"
                        pos3X8 -= animation_speed2
                        pos3Y8 -= animation_speed2
                        if pos3X8 <= 450:
                            animation_speed2 = 0
                        player(playerImg14, pos3X8, pos3Y8)
                    pos3Y2 += animation_speed1
                    if pos3Y2 >= 110:
                        animation_speed1 = 0
                    player(playerImg8, 350, pos3Y2)
                    Ans = decider3(user, computer, computer1)
                    Show_result(Ans, pos3Y2)

        if start2 and player_count == '4':
            buttonlaga(a, b)
    pygame.display.update()

pygame.quit()


# TOdo four I have to complete
