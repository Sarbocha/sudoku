import pygame
import requests
pygame.init()

width = 550
bgcolor = (255, 255, 255)
line_color = (0,0,0)
layout_color = (255,0,0)

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
layout = response.json()['board']
layout_original = [[layout[x][y] for y in range(len(layout[0]))] for x in range(len(layout))]


myfont = pygame.font.SysFont("Comic Sans MS", 30)
buffer = 5


def insert(display, position):
    i, j = position[1], position[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (layout_original[i - 1][j - 1] != 0):
                    return
                if (event.key == 48):  # checking with 0
                    layout[i - 1][j - 1] = event.key - 48
                    pygame.draw.rect(display, bgcolor, (
                    position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    pygame.display.update()
                    return
                if (0 < event.key - 48 < 10):  # We are checking for valid input
                    pygame.draw.rect(display, bgcolor, (
                    position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    value = myfont.render(str(event.key - 48), True, (0, 0, 0))
                    display.blit(value, (position[0] * 50 + 15, position[1] * 50))
                    layout[i - 1][j - 1] = event.key - 48
                    pygame.display.update()
                    return

def main():

    display = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku By Sarbocha")
    display.fill(bgcolor)


    for grid in range(0,10):
        if (grid%3 == 0):
            pygame.draw.line(display, line_color, (50 + 50 * grid, 50), (50 + 50 * grid, 500), 4)
            pygame.draw.line(display, line_color, (50, 50 + 50 * grid), (500, 50 + 50 * grid), 4)
        pygame.display.update()

        pygame.draw.line(display, line_color, (50 + 50 * grid, 50), (50 + 50 * grid, 500), 2 )
        pygame.draw.line(display, line_color, (50, 50 + 50 * grid), (500, 50 + 50 * grid), 2)
    pygame.display.update()
    for i in range(0, len(layout[0])):
        for j in range(0, len(layout[0])):
            if (0<layout[i][j]<10):
                value = myfont.render(str(layout[i][j]), True, layout_color)
                display.blit(value, ((j + 1)*50 + 15, (i+1)*50 ))
    pygame.display.update()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(display, (pos[0] // 50, pos[1] // 50))


main()


