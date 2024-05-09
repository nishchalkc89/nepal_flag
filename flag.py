import pygame as pg
from pygame.locals import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *


def triangle(vertices, color=(1, 1, 1)):
    glBegin(GL_TRIANGLES)
    glColor3fv(color)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()


def circle(center, r, color=(1, 1, 1), semi=0):
    n = 2000
    glPushMatrix()
    glColor3fv(color)
    glTranslatef(center[0], center[1], 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2fv((0, 0))
    for i in range(n):
        x = i / n * r
        y = math.sqrt(r ** 2 - x ** 2)
        if semi == 1 or semi == 0:
            glVertex2f(x, y)  # 1st quadrant
            glVertex2f(-x, y)  # 2nd quadrant
        if semi == -1 or semi == 0:
            glVertex2f(-x, -y)  # 3rd quadrant
            glVertex2f(x, -y)  # 4th quadrant
    glEnd()
    glPopMatrix()


def flag_of_Nepal():
    # Blue triangles
    triangle([(0, 1), (1.55, -0.035), (0, -0.035)], (0, 0, 1))
    triangle([(0, 0.55), (0, -0.9), (1.55, -0.9)], (0, 0, 1))
    # Red triangles
    glPushMatrix()
    glTranslatef(0.04, -0.01, 0)
    glScalef(0.95, 0.95, 0)
    triangle([(0, 1), (1.5, 0), (0, 0)], (1, 0, 0))
    triangle([(0, 0.5), (0, -0.9), (1.5, -0.9)], (1, 0, 0))
    glPopMatrix()
    # chandrama
    circle((0.4, 0.3), 0.26, semi=-1)
    circle((0.4, 0.42), 0.31, color=(1, 0, 0), semi=-1)
    circle((0.4, 0.12), 0.14, semi=1)
    glPushMatrix()
    glTranslatef(0.4, 0.13, 0)
    glRotatef(68, 0, 0, 1)
    glTranslatef(-0.4, -0.2, 0)
    for i in range(9):
        glPushMatrix()
        glTranslatef(0.4, 0.2, 0)
        glRotatef(-17 * i, 0, 0, 1)
        glTranslatef(-0.4, -0.2, 0)
        triangle([(0.34, 0.2), (0.46, 0.2), (0.4, 0.4)], (1, 1, 1))
        glPopMatrix()
    glPopMatrix()
    # surya
    circle((0.4, -0.45), 0.16)
    x, y = 0.45, -0.3
    for i in range(12):
        glPushMatrix()
        glTranslatef(0.4, -0.45, 0)
        glRotatef(-30 * i, 0, 0, 1)
        glTranslatef(-0.4, 0.45, 0)
        triangle([(0.3, -0.45), (0.5, -0.45), (0.4, -0.21)], (1, 1, 1))
        glPopMatrix()


def main():
    pg.init()
    display = (800, 600)
    surface = pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(-0.8, 0, -5)
    glScalef(1.4, 1.4, 1.4)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        flag_of_Nepal()
        pg.display.flip()
        pg.time.wait(10)


if __name__ == "__main__":
    main()
