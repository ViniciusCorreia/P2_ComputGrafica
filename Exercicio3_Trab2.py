from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import png
from math import pi, cos, sin


name="Exercicio 3 - Trab2"
# variaveis da esfera
n = 20
m = 50
r = 2.5

alpha = 1.0
beta = 0
delta_alpha = 2
delta_x = 0
delta_y = 0
delta_z = 0

def LoadTextures():
    global texture
    texture = glGenTextures(2)  # Gera 2 IDs para as texturas

    # Seleciona a imagem do dado através reader no png.py
    reader = png.Reader(filename='mapa.png')
    w, h, pixels, metadata = reader.read_flat()
    if (metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB

    glBindTexture(GL_TEXTURE_2D, texture[0])
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)



# Cacacteristicas da esfera
def f(i, j):
    theta = ((3.14 * i) / (n - 1)) - (3.14 / 2)
    phi = 2 * 3.14 * j / (n - 1)
    x = r * cos(theta) * cos(phi)
    y = r * sin(theta)
    z = r * cos(theta) * sin(phi)
    t = ((theta + (3.14 / 2)) / 3.14)
    p = (phi / (2 * 3.14))
    return x, y, z, t, p


def figure():
    glPushMatrix()
    glRotatef(alpha, 1.0, 0, 0.0)

    glBindTexture(GL_TEXTURE_2D, texture[0])
    for i in range(n):

        glBegin(GL_QUAD_STRIP)
        for j in range(m):
            x, y, z, t, p = f(i, j)
            glTexCoord2f(p, t)
            glVertex3f(x, y, z)
            x, y, z, t, p = f(i + 1, j)
            glTexCoord2f(p, t)
            glVertex3f(x, y, z)

        glEnd()
    glPopMatrix()


def desenha():
    global alpha
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    figure()
    alpha = alpha + delta_alpha
    GLUT.glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(1024, 1024)
    glutCreateWindow(name)
    glutDisplayFunc(desenha)
    LoadTextures()
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    gluPerspective(-45, 5/3, 0.1, 100.0)
    glTranslatef(0.0, 0.0, -10)
    glutTimerFunc(10, timer, 1)
    glutMainLoop()

if __name__ == '__main__':
    main()
