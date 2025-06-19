import pygame
import sys

pygame.init()

width = 300
height = 300

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Tic Tac Toe")

board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False


def check_winner(player):
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col]:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def is_board_full():
    for row in board:
        if "" in row:
            return False
    return True


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            # detect which row and column is the mouse clicked
            row = mouseY // 100
            col = mouseX // 100

            # check if the cell is free
            if board[row][col] == "" and not game_over:
                board[row][col] = current_player
                print(board)

                if check_winner(current_player):
                    print(f"Player {current_player} wins!")
                    game_over = True

                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"

            print(mouseX, mouseY)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    # pygame.draw.line(screen, (color), (start pos. x,y), (end pos. x,y), thickness)

    pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 300), 3)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 300), 3)

    pygame.draw.line(screen, (0, 0, 0), (0, 100), (300, 100), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (300, 200), 3)

    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(screen, (0, 0, 255), (col * 100 + 20, row * 100 + 20),
                                 (col * 100 + 80, row * 100 + 80), 3)
                pygame.draw.line(screen, (0, 0, 255), (col * 100 + 80, row * 100 + 20),
                                 (col * 100 + 20, row * 100 + 80), 3)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, (255, 0, 0),
                                   (col * 100 + 50, row * 100 + 50), 35, 3)
    pygame.display.update()
