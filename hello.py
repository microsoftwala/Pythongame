import time
import pygame
import random
import socket
import re
import threading

pygame.init()
# Create the screen

screen = pygame.display.set_mode((900, 580))


player1set = ''


def player2set(client, SIZE, FORMAT):
    return client.recv(SIZE).decode(FORMAT)


def player3set(client, SIZE, FORMAT):
    return client.recv(SIZE).decode(FORMAT)


def player4set(client, SIZE, FORMAT):
    return client.recv(SIZE).decode(FORMAT)


def game(client, FORMAT, SIZE):
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
    playerImg16 = pygame.transform.rotate(playerImg1, 90)
    playerImg17 = pygame.transform.rotate(playerImg2, 90)

    # Two player
    # Left
    Left_move_X = 50
    Left_move_y = 200  # not changed

    # right
    Right_move_x = 750
    Right_move_y = 200  # not changed

    # Three player
    # Top
    Top_move_x = 370  # notchanged
    Top_move_y = 0

    # leftdiagonal
    Left_Diagonal_move_x = 50
    Left_Diagonal_move_y = 400

    # right diagonal
    Right_Diagonal_move_x = 750
    Right_Diagonal_move_y = 400

    # down
    Down_move_x = 550
    Down_move_y = 370  # not changed

    start = 0  # when two player
    start1 = 0  # when three player
    start2 = 0  # when four player

    # leader board for 2 player

    def player_score2(score1, score2):
        pygame.draw.rect(screen, (250, 150, 150), (650, 60, 220, 40))
        player1_score_text = fonts2.render(
            f"Player1 Score: {score1}", True, 'white')
        screen.blit(player1_score_text, (665, 65))
        pygame.draw.rect(screen, (250, 150, 150), (650, 100, 220, 40))
        player2_score_text = fonts2.render(
            f"Player2 Score: {score2}", True, 'white')
        screen.blit(player2_score_text, (665, 105))

    # leader board for 3 player

    def player_score3(score1, score2, score3):
        pygame.draw.rect(screen, (250, 150, 150), (650, 60, 220, 40))
        player1_score_text = fonts2.render(
            f"Player1 Score: {score1}", True, 'white')
        screen.blit(player1_score_text, (665, 65))

        pygame.draw.rect(screen, (250, 150, 150), (650, 100, 220, 40))
        player2_score_text = fonts2.render(
            f"Player2 Score: {score2}", True, 'white')
        screen.blit(player2_score_text, (665, 105))

        pygame.draw.rect(screen, (250, 150, 150), (650, 140, 220, 40))
        player1_score_text = fonts2.render(
            f"Player3 Score: {score3}", True, 'white')
        screen.blit(player1_score_text, (665, 145))

    # leader board for 4 player

    def player_score4(score1, score2, score3, score4):
        pygame.draw.rect(screen, (250, 150, 150), (650, 60, 220, 40))
        player1_score_text = fonts2.render(
            f"Player1 Score: {score1}", True, 'white')
        screen.blit(player1_score_text, (665, 65))

        pygame.draw.rect(screen, (250, 150, 150), (650, 100, 220, 40))
        player2_score_text = fonts2.render(
            f"Player2 Score: {score2}", True, 'white')
        screen.blit(player2_score_text, (665, 105))

        pygame.draw.rect(screen, (250, 150, 150), (650, 140, 220, 40))
        player1_score_text = fonts2.render(
            f"Player3 Score: {score3}", True, 'white')
        screen.blit(player1_score_text, (665, 145))

        pygame.draw.rect(screen, (250, 150, 150), (650, 180, 220, 40))
        player1_score_text = fonts2.render(
            f"Player4 Score: {score4}", True, 'white')
        screen.blit(player1_score_text, (665, 185))

    # It is among two player decider

    def decider(user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif user_choice == "Rock":
            return "You win!" if computer_choice == "Scissors" else "Player2 win!"
        elif user_choice == "Paper":
            return "You win!" if computer_choice == "Rock" else "Player2 win!"
        elif user_choice == "Scissors":
            return "You win!" if computer_choice == "Paper" else "Player2 win!"

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

    # It is among four player decider

    def decider4(user_choice, player2_choice, player3_choice, player4_choice):
        choices = [user_choice, player2_choice, player3_choice, player4_choice]
        if choices.count(user_choice) == 4:
            return "It's a tie among all players!"
        elif choices.count(user_choice) == 1:
            return "You win!"  # User wins against all other players
        else:
            return "It's a tie among some players."

    fonts = pygame.font.SysFont('Georgia', 40, bold=True)
    fonts1 = pygame.font.SysFont('Georgia', 40, bold=True)
    fonts2 = pygame.font.SysFont('Georgia', 20)

    message = fonts2.render("Enter the number of player: ", True, 'white')
    surf = fonts.render('Quit', True, 'white')
    surf1 = fonts1.render('Start', True, 'white')
    back = fonts2.render("Back", True, 'white')

    # Button positions
    button_positions = {
        "Paper": (200, 500),
        "Scissors": (400, 500),
        "Rock": (600, 500),
    }

    button = pygame.Rect(600, 550, 105, 60)
    Start_button = pygame.Rect(200, 550, 115, 60)
    button5 = pygame.Rect(370, 100, 150, 40)
    back_button = pygame.Rect(820, 5, 60, 25)

    animation_speed = 0.3
    animation_speed1 = -0.3
    animation_speed2 = 0.3
    animation_speed3 = 0.3

    Player1_Score = 0
    Player2_Score = 0
    Player3_Score = 0
    Player4_Score = 0
    Player5_Score = 0
    Player6_Score = 0
    Player7_Score = 0
    Player8_Score = 0
    Player9_Score = 0

    count_player = pygame.font.SysFont('Georgia', 20, bold=True)
    player_count = ''
    on = 0
    option = 1

    # Result show after match

    def show_winner(winner):
        result = fonts2.render("Result: ", True, "white")
        screen.blit(result, (200, 50))
        result_text = fonts2.render(winner, True, "white")
        screen.blit(result_text, (300, 50))

    # Rock paper scissor button

    def buttonlaga(a, b):
        for choice, position in button_positions.items():
            if position[0] <= a <= position[0]+110 and position[1] <= b <= position[1]+60:
                pygame.draw.rect(screen, (0, 0, 100),
                                 (position[0]+5, position[1], 100, 45), border_radius=3)
                button_text = fonts2.render(choice, True, "white")
                screen.blit(button_text, (position[0] + 26, position[1] + 11))
            else:
                pygame.draw.rect(screen, (0, 100, 100),
                                 (position[0]+5, position[1], 100, 40), border_radius=3)
                button_text = fonts2.render(choice, True, "white")
                screen.blit(button_text, (position[0] + 25, position[1] + 10))

    # gradient backgrounds

    def gradientRect(screen, left_colour, right_colour, target_rect):
        gradient_surface = pygame.Surface(
            (target_rect.width, target_rect.height))
        left_color_stop = left_colour
        right_color_stop = right_colour
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
            pygame.draw.line(gradient_surface, (r, g, b),
                             (x, 0), (x, target_rect.height))
        screen.blit(gradient_surface, target_rect)

    def player(playerImg, posX, posY):
        screen.blit(playerImg, (posX, posY))

    # Choices
    choices = ["Rock", "Paper", "Scissors"]
    player1_choice = None
    player2_choice = None
    player3_choice = None
    player4_choice = None
    target_rect = pygame.Rect(0, 0, 900, 620)

    score_displayed = False
    score_displayed1 = False
    score_displayed2 = False

    options = []
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
                    running = False
                if Start_button.collidepoint(event.pos):
                    start = 1
                    start1 = 0
                    start2 = 0
                    animation_speed = 0.3
                    animation_speed1 = -0.3
                    Left_move_X = 50
                    Right_move_x = 750
                    player1_choice = None
                    player2_choice = None

                if start:  # Check if the "Start" button is clicked
                    if player1_choice is None:
                        for choice, position in button_positions.items():
                            if event.type == pygame.MOUSEBUTTONDOWN+1 and position[0] <= event.pos[0] <= position[0] + 100 and position[1] <= event.pos[1] <= position[1] + 50:
                                player1_choice = choice
                                player1set = player1_choice
                                client.send(player1set.encode(FORMAT))

                    elif player2_choice is None:
                        player2_choice = player2set(client, SIZE, FORMAT)

            if player_count == '3' and event.type == pygame.MOUSEBUTTONUP:
                if button.collidepoint(event.pos):
                    running = False
                if Start_button.collidepoint(event.pos):
                    start1 = 1
                    start = 0
                    start2 = 0
                    animation_speed = 0.3
                    animation_speed1 = 0.3
                    animation_speed2 = 0.3
                    Top_move_y = 0
                    Left_Diagonal_move_x = 50
                    Left_Diagonal_move_y = 410
                    Right_Diagonal_move_x = 650
                    Right_Diagonal_move_y = 430
                    player1_choice = None
                    player2_choice = None
                    player3_choice = None

                if start1:  # Check if the "Start" button is clicked
                    if player1_choice is None:
                        for choice, position in button_positions.items():
                            if event.type == pygame.MOUSEBUTTONDOWN+1 and position[0] <= event.pos[0] <= position[0] + 100 and position[1] <= event.pos[1] <= position[1] + 50:
                                player1_choice = choice
                                player1set = player1_choice
                                client.send(player1set.encode(FORMAT))

                    elif player2_choice is None:
                        player2_choice = player2set(client, SIZE, FORMAT)
                        options = [s for s in re.split(
                            "([A-Z][^A-Z]*)", player2_choice) if s]
                        for i in range(0, len(options)):
                            if i == 0:
                                player2_choice = options[i]
                            else:
                                player3_choice = options[i]
                        options.clear()

            if player_count == '4' and event.type == pygame.MOUSEBUTTONUP:
                if button.collidepoint(event.pos):
                    running = False
                if Start_button.collidepoint(event.pos):
                    start2 = 1
                    start1 = 0
                    start = 0
                    animation_speed = 0.3
                    animation_speed1 = 0.3
                    animation_speed2 = 0.3
                    animation_speed3 = 0.3
                    Top_move_y = 0
                    Left_move_X = 50
                    Right_move_x = 750
                    Down_move_y = 450
                    player1_choice = None
                    player2_choice = None
                    player3_choice = None
                    player4_choice = None

                if start2:  # Check if the "Start" button is clicked
                    if player1_choice is None:
                        for choice, position in button_positions.items():
                            if event.type == pygame.MOUSEBUTTONDOWN+1 and position[0] <= event.pos[0] <= position[0] + 100 and position[1] <= event.pos[1] <= position[1] + 50:
                                player1_choice = choice
                                player1set = player1_choice
                                client.send(player1set.encode(FORMAT))

                    elif player2_choice is None:
                        player2_choice = player2set(client, SIZE, FORMAT)
                        options = [s for s in re.split(
                            "([A-Z][^A-Z]*)", player2_choice) if s]
                        for i in range(0, len(options)):
                            if i == 0:
                                player2_choice = options[i]
                            elif i == 1:
                                player3_choice = options[i]
                            else:
                                player4_choice = options[i]
                        options.clear()

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
                screen.blit(surf1, (Start_button.x +
                            7.5, Start_button.y + 7.5))
            else:
                pygame.draw.rect(screen, (0, 0, 0),
                                 Start_button, border_radius=3)
                screen.blit(surf1, (Start_button.x + 5, Start_button.y + 5))

            if start and player_count == '2':
                if player1_choice == None:
                    buttonlaga(a, b)

                if player1_choice is None:
                    prompt = fonts2.render(
                        "Player 1: Choose your move", True, "white")
                    screen.blit(prompt, (50, 50))
                    player_score2(Player1_Score, Player2_Score)
                    score_displayed = True
                elif player2_choice is None:
                    pass
                else:
                    if (player2_choice != None):
                        if player1_choice == "Paper":
                            Left_move_X += animation_speed
                            if Left_move_X >= 250:
                                animation_speed = 0
                            player(playerImg, Left_move_X, 200)

                        elif player1_choice == "Scissors":
                            Left_move_X += animation_speed
                            if Left_move_X >= 250:
                                animation_speed = 0
                            player(playerImg1, Left_move_X, 200)

                        elif player1_choice == "Rock":
                            Left_move_X += animation_speed
                            if Left_move_X >= 250:
                                animation_speed = 0
                            player(playerImg2, Left_move_X, 200)

                        if player2_choice == "Paper":
                            Right_move_x += animation_speed1
                            if Right_move_x <= 550:
                                animation_speed1 = 0
                            player(playerImg3, Right_move_x, 200)

                        elif player2_choice == "Scissors":
                            Right_move_x += animation_speed1
                            if Right_move_x <= 550:
                                animation_speed1 = 0
                            player(playerImg4, Right_move_x, 200)

                        elif player2_choice == "Rock":
                            Right_move_x += animation_speed1
                            if Right_move_x <= 550:
                                animation_speed1 = 0
                            player(playerImg5, Right_move_x, 200)

                        winner = decider(player1_choice, player2_choice)
                        if winner == "You win!" and score_displayed:
                            Player1_Score += 1
                            score_displayed = False
                        elif winner == "Player2 win!" and score_displayed:
                            Player2_Score += 1
                            score_displayed = False
                        show_winner(winner)
                    player_score2(Player1_Score, Player2_Score)

            if start1 and player_count == '3':
                if player1_choice is None:
                    buttonlaga(a, b)
                if player1_choice is None:
                    prompt = fonts2.render(
                        "Player 1: Choose your move", True, "white")
                    screen.blit(prompt, (50, 50))
                    player_score3(Player3_Score, Player4_Score, Player5_Score)
                    score_displayed1 = True
                elif player2_choice is None and player3_choice is None:
                    pass
                else:
                    if player2_choice != None and player3_choice != None:
                        if player1_choice == "Paper":
                            Left_Diagonal_move_x += animation_speed
                            Left_Diagonal_move_y -= animation_speed
                            if Left_Diagonal_move_x >= 220:
                                animation_speed = 0
                            player(playerImg9, Left_Diagonal_move_x,
                                   Left_Diagonal_move_y)

                        elif player1_choice == "Scissors":
                            Left_Diagonal_move_x += animation_speed
                            Left_Diagonal_move_y -= animation_speed
                            if Left_Diagonal_move_x >= 220:
                                animation_speed = 0
                            player(playerImg10, Left_Diagonal_move_x,
                                   Left_Diagonal_move_y)

                        elif player1_choice == "Rock":
                            Left_Diagonal_move_x += animation_speed
                            Left_Diagonal_move_y -= animation_speed
                            if Left_Diagonal_move_x >= 220:
                                animation_speed = 0
                            player(playerImg11, Left_Diagonal_move_x,
                                   Left_Diagonal_move_y)

                        if player2_choice == "Paper":
                            Top_move_y += animation_speed1
                            if Top_move_y >= 150:
                                animation_speed1 = 0
                            player(playerImg6, 370, Top_move_y)

                        elif player2_choice == "Scissors":
                            Top_move_y += animation_speed1
                            if Top_move_y >= 150:
                                animation_speed1 = 0
                            player(playerImg7, 370, Top_move_y)

                        elif player2_choice == "Rock":
                            Top_move_y += animation_speed1
                            if Top_move_y >= 150:
                                animation_speed1 = 0
                            player(playerImg8, 370, Top_move_y)

                        if player3_choice == "Paper":
                            Right_Diagonal_move_x -= animation_speed2
                            Right_Diagonal_move_y -= animation_speed2
                            if Right_Diagonal_move_x <= 470:
                                animation_speed2 = 0
                            player(playerImg12, Right_Diagonal_move_x,
                                   Right_Diagonal_move_y)

                        elif player3_choice == "Scissors":
                            Right_Diagonal_move_x -= animation_speed2
                            Right_Diagonal_move_y -= animation_speed2
                            if Right_Diagonal_move_x <= 470:
                                animation_speed2 = 0
                            player(playerImg13, Right_Diagonal_move_x,
                                   Right_Diagonal_move_y)

                        elif player3_choice == "Rock":
                            Right_Diagonal_move_x -= animation_speed2
                            Right_Diagonal_move_y -= animation_speed2
                            if Right_Diagonal_move_x <= 470:
                                animation_speed2 = 0
                            player(playerImg14, Right_Diagonal_move_x,
                                   Right_Diagonal_move_y)

                        winner = decider3(
                            player1_choice, player2_choice, player3_choice)
                        if score_displayed1 and winner == "You win!":
                            Player3_Score += 1
                            score_displayed1 = False
                        if score_displayed1 and winner == "Player 2 and Player 3 tie!":
                            Player4_Score += 1
                            Player5_Score += 1
                            score_displayed1 = False

                        show_winner(winner)
                    player_score3(Player3_Score, Player4_Score, Player5_Score)

            if start2 and player_count == '4':
                if player1_choice is None:
                    buttonlaga(a, b)
                if player1_choice is None:
                    prompt = fonts2.render(
                        "Player 1: Choose your move", True, "white")
                    screen.blit(prompt, (50, 50))
                    player_score4(Player6_Score, Player7_Score,
                                  Player8_Score, Player9_Score)
                    score_displayed2 = True
                elif player2_choice is None and player3_choice is None and player4_choice is None:
                    pass

                else:
                    if player2_choice != None and player3_choice != None and player4_choice != None:
                        if player1_choice == "Paper":
                            Left_move_X += animation_speed
                            if Left_move_X >= 250:
                                animation_speed = 0
                            player(playerImg, Left_move_X, 200)

                        elif player1_choice == "Scissors":
                            Left_move_X += animation_speed
                            if Left_move_X >= 250:
                                animation_speed = 0
                            player(playerImg1, Left_move_X, 200)

                        elif player1_choice == "Rock":
                            Left_move_X += animation_speed
                            if Left_move_X >= 250:
                                animation_speed = 0
                            player(playerImg2, Left_move_X, 200)

                        if player2_choice == "Paper":
                            Top_move_y += animation_speed1
                            if Top_move_y >= 120:
                                animation_speed1 = 0
                            player(playerImg6, 380, Top_move_y)

                        elif player2_choice == "Scissors":
                            Top_move_y += animation_speed1
                            if Top_move_y >= 120:
                                animation_speed1 = 0
                            player(playerImg7, 380, Top_move_y)

                        elif player2_choice == "Rock":
                            Top_move_y += animation_speed1
                            if Top_move_y >= 120:
                                animation_speed1 = 0
                            player(playerImg8, 380, Top_move_y)

                        if player3_choice == "Paper":
                            Right_move_x -= animation_speed2
                            if Right_move_x <= 540:
                                animation_speed2 = 0
                            player(playerImg3, Right_move_x, 200)

                        elif player3_choice == "Scissors":
                            Right_move_x -= animation_speed2
                            if Right_move_x <= 540:
                                animation_speed2 = 0
                            player(playerImg4, Right_move_x, 200)

                        elif player3_choice == "Rock":
                            Right_move_x -= animation_speed2
                            if Right_move_x <= 540:
                                animation_speed2 = 0
                            player(playerImg5, Right_move_x, 200)

                        if player4_choice == "Paper":
                            Down_move_y -= animation_speed3
                            if Down_move_y <= 280:
                                animation_speed3 = 0
                            player(playerImg15, 380, Down_move_y)

                        elif player4_choice == "Scissors":
                            Down_move_y -= animation_speed3
                            if Down_move_y <= 280:
                                animation_speed3 = 0
                            player(playerImg16, 380, Down_move_y)

                        elif player4_choice == "Rock":
                            Down_move_y -= animation_speed3
                            if Down_move_y <= 280:
                                animation_speed3 = 0
                            player(playerImg17, 380, Down_move_y)

                        winner = decider4(
                            player1_choice, player2_choice, player3_choice, player4_choice)

                        if score_displayed2 and winner == "You win!":
                            Player6_Score += 1
                            score_displayed2 = False
                        show_winner(winner)
                    player_score4(Player6_Score, Player7_Score,
                                  Player8_Score, Player9_Score)

        pygame.display.update()

    pygame.quit()


def main():
    IP = '172.16.21.36'
    PORT = 8000
    ADDR = (IP, PORT)
    SIZE = 1024
    FORMAT = "utf-8"
    DISCONNECT_MSG = "BYE"

    client = socket.socket()
    client.connect(ADDR)
    print(f"[Connected] Client connected to server at {IP}:{PORT}")
    game(client, FORMAT, SIZE)


if __name__ == '__main__':
    main()
