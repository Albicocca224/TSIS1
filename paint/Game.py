from math import sqrt
from datetime import datetime
import pygame, pygame.gfxdraw
import os, random

pygame.init()
display_size = (1200, 850)
display = pygame.display.set_mode(display_size)
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

canvas_start = 35
button_size = 10
button_gap = 5

font = pygame.font.Font("C://Windows//Fonts//Arial.ttf", 18)

colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "purple": (255, 0, 255),
    "rand_col": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
}

clear_butt_text = font.render("Clear screen", True, colors["black"], (255, 255, 230))
clear_butt_rect = clear_butt_text.get_rect()
clear_butt_rect.center = (900, 10)

rectangle_selected_true = pygame.image.load('img/rectangle_selected_true.png')
rectangle_selected_false = pygame.image.load('img/rectangle_selected_false.png')
circle_selected_true = pygame.image.load('img/circle_selected_true.png')
circle_selected_false = pygame.image.load('img/circle_selected_false.png')
square_selected_true = pygame.image.load('img/rectangle_selected_true.png')
square_selected_false = pygame.image.load('img/rectangle_selected_false.png')
r_triangle_selected_true = pygame.image.load('img/rectangle_selected_true.png')
r_triangle_selected_false = pygame.image.load('img/rectangle_selected_false.png')
eq_triangle_selected_true = pygame.image.load('img/rectangle_selected_true.png')
eq_triangle_selected_false = pygame.image.load('img/rectangle_selected_false.png')
rhombus_selected_true = pygame.image.load('img/rectangle_selected_true.png')
rhombus_selected_false = pygame.image.load('img/rectangle_selected_false.png')


display.fill(colors["white"])


def get_canvas_image():
    w = display_size[0]
    h = display_size[1] - canvas_start

    canvas = pygame.Rect(0, canvas_start, w, h)
    screenshot = pygame.Surface((w, h))
    screenshot.blit(display.subsurface(canvas), (0, 0))
    return screenshot


def draw_rectangle(first_corner, second_corner):
    # first_corner = rect_pos[0] --> (a,b)
    # second_corner = rect_pos[1] --> (c,d)
    # third_corner = (first_corner[0], second_corner[1]) -->(a,d)
    # fourth_corner = (second_corner[0], first_corner[1]) -->(c,b)

    # note: first and second corners are diagonally opposite and so are third and fourth corners
    # did this because as from above the x value for all corners can either be a or c
    left_x = min(first_corner[0], second_corner[0])

    # similarly y values can either be b or d, so the left_top corner can be decided by taking least of a,b and c,d
    left_y = min(first_corner[1], second_corner[1])

    w = abs(
        first_corner[0] - second_corner[0])  # width will be the difference of x coordinates of the two opposite points
    h = abs(first_corner[1] - second_corner[1])  # same thing with the height
    return left_x, left_y, w, h
def draw_square(top_left, side_length):
    left_x = top_left[0]
    left_y = top_left[1]
    w = h = side_length  # In a square, width and height are the same
    return left_x, left_y, w, h
def draw_r_triangle(top_left, base, height):
    left_x = top_left[0]
    left_y = top_left[1]
    w = base
    h = height
    return left_x, left_y, w, h
def draw_eq_triangle(top_left, side_length):
    left_x = top_left[0]
    left_y = top_left[1]
    w = h = side_length
    return left_x, left_y, w, h
def draw_rhombus(top_left, side_length):
    left_x = top_left[0]
    left_y = top_left[1]
    w = h = side_length
    return left_x, left_y, w, h

def pen_draw(pen_color, pos, prev_pos, display, size):
    dist = sqrt((pos[0] - prev_pos[0]) ** 2 + (pos[1] - prev_pos[1]) ** 2)

    if (dist > size * 0.5):
        pygame.draw.line(display, pen_color, ((prev_pos[0]), (prev_pos[1])), ((pos[0]), (pos[1])), width=size)
        return

    pygame.draw.rect(display, pen_color, pygame.Rect((pos[0] - size // 2), (pos[1] - size // 2), size, size))


def main():
    tool_id = 0
    size = 15
    pen_color = colors['black']
    eraser_color = colors['white']
    color_button = []
    rect_pos = []
    display.blit(clear_butt_text, clear_butt_rect)

    # this draws buttons for colors
    for i in range(0, len(colors)):
        color_button.append(pygame.Rect((button_size + button_gap) * (i), button_size, button_size, button_size))
        pygame.draw.rect(display, [*colors.values()][i], color_button[i])

    # this draws the rectangle tool, (15,25)
    rectangle_rect = pygame.Rect(15, 25, 10, 10)
    circle_rect = pygame.Rect(30, 25, 10, 10)
    square_rect = pygame.Rect(45, 25, 10, 10)
    r_triangle_rect = pygame.Rect(60, 25, 10, 10)
    eq_triangle_rect = pygame.Rect(75, 25, 10, 10)
    rhombus_rect = pygame.Rect(90, 25, 10, 10)
    display.blit(rectangle_selected_false, rectangle_rect)
    display.blit(circle_selected_false, circle_rect)
    display.blit(square_selected_false, square_rect)
    display.blit(r_triangle_selected_false, r_triangle_rect)
    display.blit(eq_triangle_selected_false, eq_triangle_rect)
    display.blit(rhombus_selected_false, rhombus_rect)
    pos = (0, 0)

    while True:
        for event in pygame.event.get():
            prev_pos = pos
            pos = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                print("closing")
                quit()

            if keys[pygame.K_KP_PLUS] and size < 200:  # changing size of pen
                size += 1
            if keys[pygame.K_KP_MINUS] and size > 5:
                size -= 1

            if (keys[pygame.K_LCTRL] and keys[pygame.K_s]) or (keys[pygame.K_RCTRL] and keys[pygame.K_s]):
                image = get_canvas_image()
                date = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                pygame.image.save(image, f"{date.lower()}-image.jpg")

            if pygame.mouse.get_pressed() == (1, 0, 0):
                if clear_butt_rect.collidepoint(
                        pos):  # draws a white rectangle all over the screen and then redraws all the buttons
                    display.fill(colors["white"])
                    for i in range(0, len(colors)):
                        pygame.draw.rect(display, [*colors.values()][i], color_button[i])

                    if tool_id == 1:
                        display.blit(rectangle_selected_true, rectangle_rect)
                    else:
                        display.blit(rectangle_selected_false, rectangle_rect)

                    if tool_id == 2:
                        display.blit(circle_selected_true, circle_rect)
                    else:
                        display.blit(circle_selected_false, circle_rect)
                    if tool_id == 3:
                        display.blit(square_selected_true, square_rect)
                    else:
                        display.blit(square_selected_false, square_rect)
                    if tool_id == 4:
                        display.blit(r_triangle_selected_true, r_triangle_rect)
                    else:
                        display.blit(r_triangle_selected_false, r_triangle_rect)
                    if tool_id == 5:
                        display.blit(eq_triangle_selected_true, eq_triangle_rect)
                    else:
                        display.blit(eq_triangle_selected_false, eq_triangle_rect)
                    if tool_id == 6:
                        display.blit(rhombus_selected_true, rhombus_rect)
                    else:
                        display.blit(rhombus_selected_false, rhombus_rect)
                    display.blit(clear_butt_text, clear_butt_rect)

                # checks if any color is pressed
                for i in range(len(color_button)):
                    if color_button[i].collidepoint(pos):
                        pen_color = [*colors.values()][i]
                        break

                if rectangle_rect.collidepoint(pos):  # tool id = 0
                    print("click on the diagonally opposite ends of the rectangle you want to draw")

                    tool_id = 1 if tool_id != 1 else 0
                    rect_pos = []
                    if tool_id == 1:
                        display.blit(rectangle_selected_true, rectangle_rect)
                    else:
                        display.blit(rectangle_selected_false, rectangle_rect)

                    display.blit(circle_selected_false, circle_rect)

                if circle_rect.collidepoint(pos):  # tool id = 1
                    print("click on diametrically opposite points of the circle you want to draw")
                    tool_id = 2 if tool_id != 2 else 0
                    rect_pos = []
                    if tool_id == 2:
                        display.blit(circle_selected_true, circle_rect)
                    else:
                        display.blit(circle_selected_false, circle_rect)
                    display.blit(rectangle_selected_false, rectangle_rect)
                if square_rect.collidepoint(pos):
                    print("click on the top left corner of the square you want to draw")
                    tool_id = 3 if tool_id != 3 else 0
                    rect_pos = []
                    if tool_id == 3:
                        display.blit(rectangle_selected_true, square_rect)
                    else:
                        display.blit(rectangle_selected_false, square_rect)
                    display.blit(circle_selected_false, circle_rect)
                if r_triangle_rect.collidepoint(pos):
                    print("click on the top left corner of the right triangle you want to draw")
                    tool_id = 4 if tool_id != 4 else 0
                    rect_pos = []
                    if tool_id == 4:
                        display.blit(rectangle_selected_true, r_triangle_rect)
                    else:
                        display.blit(rectangle_selected_false, r_triangle_rect)
                    display.blit(circle_selected_false, circle_rect)
                if eq_triangle_rect.collidepoint(pos):
                    print("click on the top left corner of the equilateral triangle you want to draw")
                    tool_id = 5 if tool_id != 5 else 0
                    rect_pos = []
                    if tool_id == 5:
                        display.blit(rectangle_selected_true, eq_triangle_rect)
                    else:
                        display.blit(rectangle_selected_false, eq_triangle_rect)
                    display.blit(circle_selected_false, circle_rect)
                if rhombus_rect.collidepoint(pos):
                    print("click on the top left corner of the rhombus you want to draw")
                    tool_id = 6 if tool_id != 6 else 0
                    rect_pos = []
                    if tool_id == 6:
                        display.blit(rectangle_selected_true, rhombus_rect)
                    else:
                        display.blit(rectangle_selected_false, rhombus_rect)
                    display.blit(circle_selected_false, circle_rect)
                # main drawing part
                if tool_id:  # drawing with tools
                    if len(rect_pos) < 2 and (pos[1] - size // 2) > 35:
                        rect_pos.append(pos)

                    if len(rect_pos) == 2:
                        first_corner = rect_pos[0]  # --> (a,b)
                        second_corner = rect_pos[1]  # --> (c,d)

                        if tool_id == 1:  # this draws rectangle
                            left_x, left_y, w, h = draw_rectangle(first_corner, second_corner)
                            pygame.draw.rect(display, pen_color, pygame.Rect(left_x, left_y, w, h), size)

                        if tool_id == 2:  # this draws circle
                            center = (((first_corner[0] + second_corner[0]) // 2),
                                      ((first_corner[1] + second_corner[1]) // 2))  # mid point formula
                            radius = sqrt((center[0] - first_corner[0]) ** 2 + (
                                        center[1] - first_corner[1]) ** 2)  # distance formula(pythagoras)
                            pygame.draw.circle(display, pen_color, center, radius, size)
                        if tool_id == 3:
                            left_x, left_y, w, h = draw_square(first_corner, second_corner[0] - first_corner[0])
                            pygame.draw.rect(display, pen_color, pygame.Rect(left_x, left_y, w, h), size)
                        rect_pos = []
                        if tool_id == 4:
                            left_x, left_y, w, h = draw_r_triangle(first_corner, second_corner[0] - first_corner[0],
                                                                  second_corner[1] - first_corner[1])
                            pygame.draw.polygon(display, pen_color, [(left_x, left_y), (left_x + w, left_y),
                                                                    (left_x, left_y + h)], size)
                        if tool_id == 5:
                            left_x, left_y, w, h = draw_eq_triangle(first_corner, second_corner[0] - first_corner[0])
                            pygame.draw.polygon(display, pen_color, [(left_x, left_y), (left_x + w, left_y),
                                                                    (left_x + w // 2, left_y + h)], size)
                        if tool_id == 6:
                            left_x, left_y, w, h = draw_rhombus(first_corner, second_corner[0] - first_corner[0])
                            pygame.draw.polygon(display, pen_color, [(left_x + w // 2, left_y), (left_x + w, left_y + h // 2),
                                                                    (left_x + w // 2, left_y + h), (left_x, left_y + h // 2)], size)

                if (pos[1] - size // 2) > canvas_start and tool_id == 0:
                    pen_draw(pen_color, pos, prev_pos, display, size)
                    # pygame.draw.rect(display, pen_color, pygame.Rect((pos[0]-size//2), (pos[1]-size//2), size, size))
                    # pygame.draw.line(display, pen_color, ((prev_pos[0]-size//2), (prev_pos[1]-size//2)), ((pos[0]-size//2), (pos[1]-size//2)), width=size)

            if pygame.mouse.get_pressed() == (0, 0, 1):
                if (pos[1] - size // 2) > 20 and (pos[0] - size // 2) > 30:
                    # pygame.draw.rect(display, eraser_color, pygame.Rect(((pos[0]-size//2), (pos[1]-size//2), size, size)))
                    pygame.draw.line(display, eraser_color, ((prev_pos[0] - size // 2), (prev_pos[1] - size // 2)),
                                     ((pos[0] - size // 2), (pos[1] - size // 2)), width=size)

        pygame.display.update()
        clock.tick(240)


main()
quit()