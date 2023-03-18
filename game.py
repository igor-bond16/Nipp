import pygame
import sys
import math
from settings import *

pygame.init()


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # self.win.blit(GAME_BOARD, (0, 0))
            self.win.fill(BOARD_COLOR)

            pygame.draw.line(
                self.win, BLACK_COLOR, (5 * SQUARE_SIZE + SQUARE_SIZE // 2, SQUARE_SIZE // 2), (7 * SQUARE_SIZE + SQUARE_SIZE // 2, 2*SQUARE_SIZE + SQUARE_SIZE // 2), 3)
            pygame.draw.line(
                self.win, BLACK_COLOR, (SQUARE_SIZE // 2, 2*SQUARE_SIZE + SQUARE_SIZE // 2), (2 * SQUARE_SIZE + SQUARE_SIZE // 2, SQUARE_SIZE // 2), 3)
            pygame.draw.line(
                self.win, BLACK_COLOR, (SQUARE_SIZE // 2, 5*SQUARE_SIZE + SQUARE_SIZE // 2), (2*SQUARE_SIZE + SQUARE_SIZE // 2, 7*SQUARE_SIZE + SQUARE_SIZE // 2), 3)
            pygame.draw.line(
                self.win, BLACK_COLOR, (5*SQUARE_SIZE + SQUARE_SIZE // 2, 7*SQUARE_SIZE + SQUARE_SIZE // 2), (7*SQUARE_SIZE + SQUARE_SIZE // 2, 5*SQUARE_SIZE + SQUARE_SIZE // 2), 3)

            for row in range(ROWS):
                for col in range(COLS):
                    if board[row][col] != 2:
                        x = col * SQUARE_SIZE + SQUARE_SIZE // 2
                        y = row * SQUARE_SIZE + SQUARE_SIZE // 2

                        # Draw the cell
                        pygame.draw.circle(
                            self.win, WHITE_COLOR, (x, y), PIECE_RADIUS//3, 2)
                        if col < COLS - 1 and not (board[row][col + 1] == 2):
                            x2 = x + SQUARE_SIZE
                            y2 = y
                            pygame.draw.line(
                                self.win, BLACK_COLOR, (x, y), (x2, y2), 3)

                        # Draw the vertical line below the cell
                        if row < ROWS - 1 and not (board[row+1][col] == 2):
                            x2 = x
                            y2 = y + SQUARE_SIZE
                            pygame.draw.line(
                                self.win, BLACK_COLOR, (x, y), (x2, y2), 3)

                        if board[row][col] == BLACK:
                            pygame.draw.circle(
                                self.win, BLACK_COLOR, (x, y), PIECE_RADIUS)
                        elif board[row][col] == WHITE:
                            pygame.draw.circle(
                                self.win, WHITE_COLOR, (x, y), PIECE_RADIUS)

            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()

# import pygame

# # Define the size of the game board
# board_size = (400, 400)

# # Define the size of each cell on the board
# cell_size = 50

# # Define the number of rows and columns on the board
# num_rows = 7
# num_cols = 7

# # Initialize Pygame
# pygame.init()

# # Create a Pygame window
# screen = pygame.display.set_mode(board_size)

# # Define the colors to use for the board and the cells
# board_color = (255, 255, 255)  # white
# cell_color = (0, 0, 0)  # black
# line_color = (255, 0, 0)  # red

# # Define the radius of each cell
# cell_radius = cell_size // 2 - 5

# # Fill the screen with the board color
# screen.fill(board_color)

# # Draw the cells on the board
# for row in range(num_rows):
#     for col in range(num_cols):
#         # Calculate the x and y coordinates of the center of the cell
#         x = col * cell_size + cell_size // 2
#         y = row * cell_size + cell_size // 2

#         # Draw the cell
#         pygame.draw.circle(screen, cell_color, (x, y), cell_radius)

#         # Draw the horizontal line to the right of the cell
#         if col < num_cols - 1:
#             x2 = x + cell_size // 2
#             y2 = y
#             pygame.draw.line(screen, line_color, (x, y), (x2, y2), 3)

#         # Draw the vertical line below the cell
#         if row < num_rows - 1:
#             x2 = x
#             y2 = y + cell_size // 2
#             pygame.draw.line(screen, line_color, (x, y), (x2, y2), 3)

# # Update the Pygame window
# pygame.display.flip()

# # Wait for the user to close the window
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
