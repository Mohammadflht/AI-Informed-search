import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 540
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 40

# Create a Pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

# Load font
font = pygame.font.Font(None, FONT_SIZE)


def draw_grid():
    for i in range(GRID_SIZE + 1):
        thickness = 4 if i % 3 == 0 and i > 0 else 1
        pygame.draw.line(window, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)
        pygame.draw.line(window, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)


def draw_numbers(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] != 0:
                number = font.render(str(grid[i][j]), True, BLACK)
                window.blit(number, (j * CELL_SIZE + 20, i * CELL_SIZE + 15))


def ui_ai(grid):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(WHITE)
        draw_grid()
        draw_numbers(grid)

        pygame.display.flip()
